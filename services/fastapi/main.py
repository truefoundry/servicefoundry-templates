import logging
import os

import servicefoundry

logger = logging.getLogger(__name__)

app = servicefoundry.fast_api()
print(os.environ)


@app.get(path="/add")
def add(a: int, b: int):
    return a + b


@app.get(path="/subtract")
def subtract(a: int, b: int):
    return a - b
