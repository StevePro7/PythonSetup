from pathlib import Path
import importlib

from ServiceRegistry import ServiceRegistry


def build_game():

    ServiceRegistry.clear()

    base_dir = Path(__file__).resolve().parent
    folder_managers = "Managers"
    managers_path = base_dir / "Managers"

    for file in managers_path.glob("*Manager.py"):

        if file.stem == "__init__":
            continue

        module_name = file.stem

        module = importlib.import_module(f"{folder_managers}.{module_name}")

        manager_class = getattr(module, module_name)

        ServiceRegistry.register(
            manager_class.__name__,
            manager_class()
        )

    return ServiceRegistry  # 👈 key improvement
