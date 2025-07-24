import os
def get_app_mode() -> str:
    app_mode = os.getenv("APP_MODE")
    return app_mode.lower()
