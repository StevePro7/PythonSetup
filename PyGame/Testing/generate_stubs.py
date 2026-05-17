import os
import importlib
import inspect
from ServiceRegistry import ServiceRegistry


MANAGERS_DIR = "Managers"
OUTPUT_FILE = "MyGame.pyi"


def discover_managers():
    managers = {}

    for file in os.listdir(MANAGERS_DIR):
        if not file.endswith(".py") or file.startswith("__"):
            continue

        module_name = file[:-3]  # strip .py
        module_path = f"{MANAGERS_DIR}.{module_name}"

        module = importlib.import_module(module_path)

        # find class inside module
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # ensure class belongs to this module (not imported)
            if obj.__module__ == module_path:
                managers[name] = obj

    return managers


def generate_pyi(managers):
    lines = []

    # ---- imports for IDE navigation ----
    for name, cls in managers.items():
        lines.append(f"from Managers.{name} import {name}")

    lines.append("")
    lines.append("")
    lines.append("class MyGame:")
    lines.append("    @staticmethod")
    lines.append("    def Construct(): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def Initialize(): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def LoadContent(): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def Update(game_time: float): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def Draw(): ...")
    lines.append("")
    lines.append("    class Manager:")
    lines.append("        ...")

    # ---- manager declarations ----
    for name, cls in managers.items():
        lines.append(f"        {name}: {name}")

    content = "\n".join(lines)

    with open(OUTPUT_FILE, "w") as f:
        f.write(content)

    print(f"Generated {OUTPUT_FILE} with {len(managers)} managers")


if __name__ == "__main__":
    # optional: ensure registry is populated before generation
    managers = discover_managers()

    # register for runtime system
    for name, cls in managers.items():
        ServiceRegistry.register(name, cls())

    generate_pyi(managers)