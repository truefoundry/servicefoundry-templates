import logging
import servicefoundry
import mlflow
import numpy as np

from typing import List


logger = logging.getLogger(__name__)

app = servicefoundry.fast_api()
model = mlflow.sklearn.load_model("model/")


@app.get(path="/predict")
def predict(a: List):
    return model.predict(np.array(a))


@app.get("/")
def root():
    return {"message": "Hello World"}
