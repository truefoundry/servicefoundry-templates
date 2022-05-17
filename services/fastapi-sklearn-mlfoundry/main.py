import logging
from servicefoundry.service import fastapi
import mlflow
import numpy as np

from typing import List


logger = logging.getLogger(__name__)

app = fastapi.app()
model = mlflow.sklearn.load_model("model/")


@app.post(path="/predict")
def predict(a: List):
    ret = model.predict(np.array(a))
    return ret.tolist()


@app.get("/")
def root():
    return {"message": "Hello World"}
