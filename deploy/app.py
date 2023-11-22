from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import numpy as np
import cv2
import os
from io import BytesIO
from load_models import Model
from datetime import datetime


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


class Info:
    def __init__(self, cwd, models_dir, default_model_name):
        self.cwd = cwd
        self.models_dir = models_dir
        self.default_model_name = default_model_name

    def set_Default_model_name(self, default_model_name):
        self.default_model_name = default_model_name

    def set_Models_dir(self, models_dir):
        self.models_dir = models_dir


class ModelPlaceholder:
    def __init__(self, info: Info):
        self.info = info
        self.model = Model(
            info.cwd, os.path.join(info.models_dir, info.default_model_name + ".yml")
        )

    def set_Info(self, info: Info):
        self.info = info

    def change_model(self, model_name):
        ans = dict()
        if model_name.startswith("HAT-S"):
            try:
                for file_name in os.listdir(info.models_dir):
                    if model_name in file_name:
                        self.model = Model(
                            info.cwd,
                            os.path.join(self.info.models_dir, model_name + ".yml"),
                        )
                        ans["status"] = "success"
                        ans["msg"] = (
                            "Model has changed: " + info.default_model_name + ".yml"
                        )
                        return ans
                ans["status"] = "failed"
                ans["msg"] = "Can't find model!"
            except:
                ans["status"] = "failed"
                ans["msg"] = "Cannot change model!"
        else:
            ans["status"] = "failed"
            ans["msg"] = "Invalid data!"
        return ans


class FeedbackPlaceholder:
    def __init__(self):
        self.file_path = "feedbacks.txt"

    def add_feedback(self, text):
        file = open(self.file_path, "a")
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + " | " + text + "\n")
        file.close()
        print(f"Received feedback: {text}")

    def send_feedback(self, time):
        n = len(time)
        result = []
        try:
            file = open(self.file_path, "r")
            while True:
                line = file.readline().strip()
                if not line:
                    break
                if line[:n] > time:
                    result.append(line)
            file.close()
            return "\n".join(result)
        except:
            return ""

    def clear(self):
        try:
            file = open(self.file_path, "w")
            file.close()
            return "success"
        except:
            return "Delete feedbacks failure!"


class LogPlaceholder:
    def __init__(self):
        self.file_path = "logs.txt"

    def add_log(self, text):
        file = open(self.file_path, "a")
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + " | " + text + "\n")
        file.close()
        print(f"Saved log: {text}")

    def send_log(self, time):
        n = len(time)
        result = []
        try:
            file = open(self.file_path, "r")
            while True:
                line = file.readline().strip()
                if not line:
                    break
                if line[:n] > time:
                    result.append(line)
            return "\n".join(result)
        except:
            return ""

    def clear(self):
        try:
            file = open(self.file_path, "w")
            file.close()
            return "success"
        except:
            return "Delete logs failure!"


@app.route("/")
def hello():
    return "All is well if you see this line!"


@app.route("/admin", methods=["POST"])
def admin():
    result = dict()
    try:
        request_type = request.form.get("request", "")
        request_time = request.form.get("time", "")
        try:
            if request_type == "feedback":
                result["feedback"] = feedbackPlaceholder.send_feedback(request_time)
            elif request_type == "del_feedback":
                try:
                    file = open("password.txt", "r")
                    line = file.readline().strip()
                    if line == request_time:
                        result["del_feedback"] = feedbackPlaceholder.clear()
                    else:
                        result["del_feedback"] = "Wrong password!"
                except:
                    result["del_feedback"] = "Wrong password!"
            elif request_type == "password":
                try:
                    file = open("password.txt", "r")
                    line = file.readline().strip()
                    if line == request_time:
                        result["password"] = "correct"
                    else:
                        result["password"] = "wrong"
                except:
                    result["password"] = "wrong"
            elif request_type == "log":
                result["log"] = logPlaceholder.send_log(request_time)
            elif request_type == "del_log":
                try:
                    file = open("password.txt", "r")
                    line = file.readline().strip()
                    if line == request_time:
                        result["del_log"] = logPlaceholder.clear()
                    else:
                        result["del_log"] = "Wrong password!"
                except:
                    result["del_log"] = "Wrong password!"
            else:
                result["error"] = "Request type is wrong!"
        except:
            result["error"] = "Something's wrong!"
    except:
        result["error"] = "The request is not in the correct format!"
    return jsonify(result)


@app.route("/feedback", methods=["POST"])
def feedback():
    result = dict()
    try:
        feedbackText = request.form.get("feedback", "")
        try:
            feedbackPlaceholder.add_feedback(feedbackText)
            result["status"] = "success"
            result["msg"] = "Received feedback successfully!"
        except:
            result["status"] = "failed"
            result["msg"] = "Your response could not be saved!"
    except:
        result["status"] = "failed"
        result["msg"] = "The request is not in the correct format!"
    logPlaceholder.add_log("POST /feedback | " + str(result))
    return jsonify(result)


@app.route("/upload", methods=["POST"])
def upload():
    result = dict()
    try:
        image_data = request.files["image"]
        file_name = request.files["image"].filename
        model_name = request.form.get("model_name", "")
        try:
            try:
                if model_name != info.default_model_name:
                    status = model_placeholder.change_model(model_name)
                    if status["status"] == "success":
                        info.set_Default_model_name(model_name)
                        model_placeholder.set_Info(info)
                    else:
                        logPlaceholder.add_log(
                            f"POST /upload | {model_name} | {file_name} | "
                            + str(status)
                        )
                        return jsonify(status)
            except:
                result["status"] = "failed"
                result["msg"] = "Cannot change model!"
                logPlaceholder.add_log(
                    f"POST /upload | {model_name} | {file_name} | " + str(result)
                )
                return jsonify(result)

            pil_image = Image.open(image_data)
            numpy_array = np.asarray(pil_image)
            cv2_image = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2BGR).astype(float) / 255
            try:
                sr_cv2_img = model_placeholder.model.process(cv2_image)
                np_array = cv2.cvtColor(sr_cv2_img, cv2.COLOR_BGR2RGB)
                sr_pil_image = Image.fromarray(np_array)

                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d_%H-%M-%S_")
                sr_pil_image.save("SR_images/" + current_time + file_name)

                result["status"] = "success"
                result["msg"] = "Successfully increase photo quality!"
                logPlaceholder.add_log(
                    f"POST /upload | {model_name} | {file_name} | " + str(result)
                )
                return send_file(
                    "SR_images/" + current_time + file_name, mimetype="image/png"
                )
            except:
                result["status"] = "failed"
                result["msg"] = "The model encountered an error!"
        except:
            result["status"] = "failed"
            result["msg"] = "Image data cannot be read!"
    except:
        result["status"] = "failed"
        result["msg"] = "The request is not in the correct format!"
    logPlaceholder.add_log("POST /upload | " + str(result))
    return jsonify(result)


if __name__ == "__main__":
    cwd = os.getcwd()
    info = Info(
        cwd=cwd,
        models_dir=os.path.join(cwd, "options"),
        default_model_name="HAT-S_SRx4_from_scratch",
    )
    model_placeholder = ModelPlaceholder(info)
    feedbackPlaceholder = FeedbackPlaceholder()
    logPlaceholder = LogPlaceholder()
    logPlaceholder.add_log("Default model name: " + model_placeholder.model.opt["name"])
    app.run(port=5000)
