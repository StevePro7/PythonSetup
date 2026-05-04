import json
from app.infrastructure.app_context import AppContext
from app.services.scoring_service import ScoringService


class ScoringController:
    def __init__(self, context: AppContext) -> None:
        self._service = ScoringService(context)

    def handle(self, raw_data: str) -> dict:
        try:
            payload = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
            result = self._service.score(payload)
            return {
                "success": True,
                "result": result
            }
        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }
