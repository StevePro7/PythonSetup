from app.infrastructure.app_context import AppContext

class ScoringService:

    def __init__(self, context: AppContext) -> None:
        self._model = context.model


    def score(self, payload: dict):
        if "data" not in payload:
            raise ValueError("Missing required field: data")

        # TODO
        prediction = self._model.predict()
        return prediction