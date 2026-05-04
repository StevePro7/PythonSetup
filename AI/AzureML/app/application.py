from app.controllers.scoring_controller import ScoringController


class Application:
    def __init__(self, controller: ScoringController) -> None:
        self._controller = controller

    def handle(self, raw_data: str) -> dict:
        return self._controller.handle(raw_data)
