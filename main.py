from fastapi import FastAPI
import asyncio
import aiohttp
import cv2
from openvino.runtime import Core
import io
import numpy as np

app = FastAPI()

ie = Core()
model = ie.read_model(model="model/v3-small_224_1.0_float.xml")
compiled_model = ie.compile_model(model=model, device_name="CPU")

output_layer = compiled_model.output(0)


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            arr = np.fromstring(data, np.uint8)
            return cv2.imdecode(arr, cv2.IMREAD_COLOR)


def preprocess_image(src):
    image = cv2.cvtColor(src, code=cv2.COLOR_BGR2RGB)
    input_image = cv2.resize(src=image, dsize=(224, 224))
    return np.expand_dims(input_image, 0)


def infer_on(input_image):

    result_infer = compiled_model([input_image])[output_layer]
    result_index = np.argmax(result_infer)
    # Convert the inference result to a class name.
    imagenet_classes = open("utils/imagenet_2012.txt").read().splitlines()

    # The model description states that for this model, class 0 is a background.
    # Therefore, a background must be added at the beginning of imagenet_classes.
    imagenet_classes = ["background"] + imagenet_classes

    return imagenet_classes[result_index]


@app.get("/")
async def root(url: str):
    original = await download_image(url)
    input_image = preprocess_image(original)
    return infer_on(input_image)
