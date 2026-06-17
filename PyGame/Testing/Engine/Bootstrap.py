from pathlib import Path
import importlib

from Engine.ServiceRegistry import ServiceRegistry
from Game.Static import Constants as const


def build_game():

    ServiceRegistry.clear()

    base_dir = Path(__file__).resolve().parent.parent
    managers_path = base_dir / const.GAME_DIRECTORY / const.ENGINE_MANAGERS

    for file in managers_path.glob(f"*{const.ENGINE_MANAGER}.py"):

        if file.stem == "__init__":
            continue

        module_name = file.stem
        path_name = f"{const.GAME_DIRECTORY}.{const.ENGINE_MANAGERS}.{module_name}"
        module = importlib.import_module(path_name)

        manager_class = getattr(module, module_name)
        ServiceRegistry.register(
            manager_class.__name__,
            manager_class()
        )

    return ServiceRegistry
