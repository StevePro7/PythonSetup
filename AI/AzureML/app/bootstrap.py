from application import Application
from app.controllers.scoring_controller import ScoringController
from app.infrastructure.app_context import AppContext, build_app_context


def build_app() -> Application:
    context: AppContext = build_app_context()
    controller: ScoringController = ScoringController(context)
    return Application(controller)