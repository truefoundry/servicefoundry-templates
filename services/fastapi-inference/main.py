import logging
import servicefoundry

logger = logging.getLogger(__name__)

app = servicefoundry.fast_api()


@app.get("/")
def root():
    return {"message": "Hello World"}


try:
    from inference import inference
    inference(app)
except ImportError as error:
    print(error.__class__.__name__ + ": " + error.message)
    raise error



