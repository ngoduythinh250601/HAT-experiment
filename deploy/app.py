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

@app.route("/change_model", methods=["POST"])
def change_model():
    ans = dict()
    try:
        data = request.get_json()
        try:
            if 'modelName' in data and data['modelName']:
                model_name = data['modelName']
                try:
                    for file_name in models_dir:
                        if model_name in file_name:
                            model = Model(os.path.join(models_dir, file_name))
                            print("Model has been changed:", model.model.opt['name'])
                    ans["status"] = "success"
                    ans["msg"] = "model had changed: " + model_name
                except:
                    ans["status"] = "failed"
                    ans["msg"] = "can't change model"
            else:
                raise Exception()
        except:
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
            numpy_array = cv2.cvtColor(sr_cv2_img, cv2.COLOR_BGR2RGB)
            sr_pil_image = Image.fromarray(numpy_array)
            result["status"] = "success"
            result["msg"] = "success"
            image_bytes = BytesIO()
            print(image_bytes)
            sr_pil_image.save(image_bytes, format='png')
            image_bytes.seek(0)
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
    models_dir = "E:/HAT-main/deploy/options"
    default_model_name = "HAT-S_SRx4_Patch-Mosaic"
    model = Model(os.path.join(models_dir, default_model_name + '.yml'))
    print("Default model name:", model.model.opt['name'])
    app.run()