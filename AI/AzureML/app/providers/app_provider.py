from threading import Lock
from typing import Optional

from app.application import Application
from app.bootstrap import build_app


class AppProvider:
    def __init__(self) -> None:
        self._app: Optional[Application] = None
        self._lock: Lock = Lock()

    def get_app(self) -> Application:
        app = self._app
        if app is not None:
            return app

        with self._lock:
            app = self._app
            if app is None:
                app = build_app()
                self._app = app
            return app
