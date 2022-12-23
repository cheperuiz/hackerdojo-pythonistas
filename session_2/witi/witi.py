from openvino.runtime import Core
import cv2
import numpy as np


class Witi:
    """
    What Is This Image? A simple wrapper for image classification with Intel OpenVINO.
    """

    def __init__(
        self,
        model: str = "./model/v3-small_224_1.0_float.xml",
        labels: str = "./model/imagenet_2012.txt",
    ):

        self._ie = Core()
        loaded_model = self._ie.read_model(model=model)
        self._model = self._ie.compile_model(loaded_model, device_name="CPU")
        self._output_layer = self._model.output(0)
        with open(labels) as f:
            _labels = f.read().splitlines()
            self._labels = ["background"] + _labels

    def predict(self, filename: str) -> str:
        image = cv2.cvtColor(cv2.imread(filename), code=cv2.COLOR_BGR2RGB)
        input_image = cv2.resize(src=image, dsize=(224, 224))
        input_image = np.expand_dims(input_image, 0)
        predictions = self._model(input_image)[self._output_layer]  # type: ignore
        pred_index = np.argmax(predictions)
        return self._labels[pred_index]
