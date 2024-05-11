from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.utils import decodeImage
from predict.predict import DogCat
from src.logger import logging
from src.exception import CustomException
import numpy as np

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    logging.info("ClientApp Class initiated.")
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = DogCat(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
logging.info("Sucessfully rendered home page.")

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    logging.info("Prediction route initiated!")
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predictiondogcat()
        return jsonify(result)
    except CustomException as e:
        logging.info(e)
        raise(e)

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=5000)