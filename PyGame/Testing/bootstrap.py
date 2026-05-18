from pathlib import Path
import importlib

from ServiceRegistry import ServiceRegistry


def build_game():
    folder_managers: str = "Managers"
    managers_path = Path(folder_managers)

    # Iterate through all *Manager.py files
    for file in managers_path.glob("*Manager.py"):

        # Skip __init__.py if needed
        if file.stem == "__init__":
            continue

        module_name = file.stem

        # Import module dynamically
        module = importlib.import_module(f"{folder_managers}.{module_name}")

        # Get class from module
        manager_class = getattr(module, module_name)

        # Create instance and register
        ServiceRegistry.register(
            manager_class.__name__,
            manager_class()
        )

        #print(f"Registered: {manager_class.__name__}")

    return True
