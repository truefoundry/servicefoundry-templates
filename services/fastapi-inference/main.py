import logging
from servicefoundry.service import fastapi

logger = logging.getLogger(__name__)

app = fastapi.app()


@app.get("/")
def root():
    return {"message": "Hello World"}


try:
    from predict import predict
    app.add_api_route("/predict", predict)
except ImportError as error:
    print("Failed to import predict: " + error.message)
    raise error

