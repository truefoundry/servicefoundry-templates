import logging
import os

from servicefoundry.service import fastapi

logger = logging.getLogger(__name__)

app = servicefoundry.app()
print(os.environ)


@app.get(path="/add")
def add(a: int, b: int):
    return a + b


@app.get(path="/subtract")
def subtract(a: int, b: int):
    return a - b


@app.get("/")
def root():
    return {"message": "Hello World"}
