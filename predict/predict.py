import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

from src.logger import logging
from src.exception import CustomException

class DogCat:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model(os.path.join("model", "model.h5"))
        logging.info("Class DogCat initiated. Model loaded successfully.")

    
    def predictiondogcat(self):
        try:
            imagename = self.filename
            image_path = r'D:\DataScience\ComputerVision\ImageClassificationProject\inputImage.jpg'
            test_image = image.load_img(image_path, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            logging.info("Preprocessed the image... Generating results...")
            
            result = self.model(test_image)
            logging.info("Results are generated")
            logging.info(result)
            result=result.numpy()
            prediction=["dog" if result[0][0]> result[0][1] else if result[0][1] > result[0][0] "cat" else "undefined" ]
            result = [{"image": prediction}]

            return result
        
        except CustomException as e:
            logging.info(e)
            print(e)
