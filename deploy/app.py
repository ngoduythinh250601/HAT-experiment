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
    def __init__(self, cwd, models_dir, default_model_name):
        self.cwd = cwd
        self.models_dir = models_dir
        self.default_model_name = default_model_name
    
    def set_Default_model_name(self, default_model_name):
        self.default_model_name = default_model_name
        
    def set_Models_dir(self, models_dir):
        self.models_dir = models_dir

class ModelPlaceholder:
    def __init__(self, info : Info):
        self.info = info
        self.model = Model(info.cwd, os.path.join(info.models_dir, info.default_model_name + '.yml'))
        
    def set_Info(self, info : Info):
        self.info = info

    def change_model(self, model_name):
        ans = dict()
        if model_name.startswith("HAT-S"):
            try:
                for file_name in os.listdir(info.models_dir):
                    if model_name in file_name:
                        self.model = Model(info.cwd, os.path.join(self.info.models_dir, model_name + '.yml'))
                        ans["status"] = "success"
                        ans["msg"] = "Model has changed: " + info.default_model_name + ".yml"
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
 

@app.route('/')
def hello():
   return 'All is well if you see this line!'


@app.route("/upload", methods=["POST"])
def upload():
    result = dict()
    try:
        image_data = request.files['image']
        model_name = request.form.get('model_name', '')
        print(request.files)
        print(f"model_name = {model_name}")
        try:
            try:
                if (model_name != info.default_model_name):
                    status = model_placeholder.change_model(model_name)
                    if (status["status"] == "success"):
                        print("Model has changed:", model_placeholder.model.opt['name'])
                        info.set_Default_model_name(model_name)
                        model_placeholder.set_Info(info)
                    else:
                        print(status)
                        return jsonify(status)
            except:
                result["status"] = "failed"   
                result["msg"] = "Cannot change model!"
                print(result)
                return jsonify(result)

            pil_image = Image.open(image_data)
            numpy_array = np.asarray(pil_image)
            cv2_image = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2BGR).astype(float) / 255
            try:
                sr_cv2_img = model_placeholder.model.process(cv2_image)
                np_array = cv2.cvtColor(sr_cv2_img, cv2.COLOR_BGR2RGB)
                sr_pil_image = Image.fromarray(np_array)
                
                image_bytes = BytesIO()
                sr_pil_image.save(image_bytes, format='png')
                image_bytes.seek(0)
                
                result["status"] = "success"
                result["msg"] = "success"
                print("Successfully increase photo quality! Returning...")
                return send_file(image_bytes, mimetype='image/png')
            except:
                result["status"] = "failed"   
                result["msg"] = "Insufficient GPU memory!"
        except:
            result["status"] = "failed"   
            result["msg"] = "Image data cannot be read!"
    except:
        result["status"] = "failed"   
        result["msg"] = "The request is not in the correct format!"
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    cwd = os.getcwd()
    info = Info(cwd=cwd, models_dir=os.path.join(cwd,"options"), default_model_name="HAT-S_SRx4_from_scratch")
    model_placeholder = ModelPlaceholder(info)
    print("Default model name:", model_placeholder.model.opt['name'])
    app.run(port=5000)