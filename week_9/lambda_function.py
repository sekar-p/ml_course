from PIL import Image
from urllib import request
from io import BytesIO
import numpy as np
# import tensorflow.lite as tflite - Got an error when using with docker image

import tflite_runtime.interpreter as tflite


interpreter = tflite.Interpreter(model_path='cats-dogs-v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


def preprocess_input(prepared_image):
    x = np.array(prepared_image, dtype='float32')
    x = np.array([x])
    x /= 255
    return x

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def predict(url):
    downloaded_image = download_image(url)
    prepared_image = prepare_image(downloaded_image, (150, 150))
    X = preprocess_input(prepared_image)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return float_predictions


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
