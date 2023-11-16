from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
from PIL import Image
import numpy as np
import cv2
import os
from io import BytesIO
from load_models import Model


app  = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Info:
    def __init__(self, models_dir, default_model_name):
        self.models_dir = models_dir
        self.default_model_name = default_model_name
    
    def set_Default_model_name(self, default_model_name):
        self.default_model_name = default_model_name
        
    def set_Models_dir(self, models_dir):
        self.models_dir = models_dir


@app.route('/')
def hello():
   return 'All is well if you see this line!'


@app.route("/change_model", methods=["POST"])
def change_model():
    ans = dict()
    try:
        data = request.get_json()
        print("request from user: ", data)
        if str(data['modelName']).startswith("HAT-S"):
            model_name = str(data['modelName'])
            if info.default_model_name == model_name:
                ans["status"] = "success"
                ans["msg"] = "model had changed: " + model_name
                return jsonify(ans)
            try:
                for file_name in os.listdir(info.models_dir):
                    if model_name in file_name:
                        model = Model(cwd, os.path.join(info.models_dir, file_name))
                        print("Model has been changed:", model.model.opt['name'])
                        ans["status"] = "success"
                        ans["msg"] = "model had changed: " + model_name + ".yml"
                        info.default_model_name = model_name
                        return jsonify(ans)
                ans["status"] = "failed"
                ans["msg"] = "can't find model"
            except:
                ans["status"] = "failed"
                ans["msg"] = "can't change model"
        else:
            ans["status"] = "failed"
            ans["msg"] = "invalid data"
    except:
        ans["status"] = "failed"
        ans["msg"] = "fetch issue"
    return jsonify(ans)

@app.route("/upload", methods=["POST"])
def upload():
    result = dict()
    try:
        data = request.files['image']
        pil_image = Image.open(data)
        numpy_array = np.asarray(pil_image)
        cv2_image = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2BGR).astype(float) / 255
        
        try:
            sr_cv2_img = model.process(cv2_image)
            np_array = cv2.cvtColor(sr_cv2_img, cv2.COLOR_BGR2RGB)
            sr_pil_image = Image.fromarray(np_array)
            
            image_bytes = BytesIO()
            sr_pil_image.save(image_bytes, format='png')
            image_bytes.seek(0)
            
            result["status"] = "success"
            result["msg"] = "success"
            return send_file(image_bytes, mimetype='image/png')
            # result["img"] = sr_pil_image
        except:
            result["status"] = "failed"   
            result["msg"] = "model process encountered a problem"
    except:
        result["status"] = "failed"   
        result["msg"] = "image loading problem"
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    cwd = os.getcwd()
    info = Info(models_dir=os.path.join(cwd,"options"), default_model_name="HAT-S_SRx4_from_scratch")
    model = Model(cwd, os.path.join(info.models_dir, info.default_model_name + '.yml'))
    print("Default model name:", model.model.opt['name'])
    app.run(port=5000)