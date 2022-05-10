
def inference(app):
    import mlfoundry as mlf
    import pandas as pd
    import logging
    logger = logging.getLogger(__name__)

    mlf_api = mlf.get_client(api_key="MTBlYTI5MTctZDZmMC00NmNjLWI0ZmItY2NiNTk1ZDExNzlmOjU2ZjU1YQ==")
    run_id = '8da250323bdd472d868e62cf488e5a49'
    mlf_run = mlf_api.get_run(run_id)
    model = mlf_run.get_model()

    @app.post("/predict")
    def predict(a: float, b: float, c: float, d: float):
        logger.info(f"Loaded sklearn model for run_id {run_id}")
        class_name_map = dict(
            zip([0, 1, 2], ["Iris Setosa", "Iris Versicolour", "Iris Virginica"])
        )
        features = pd.DataFrame([[a, b, c, d]])
        model_output = model.predict(features)[0]
        return class_name_map[model_output]