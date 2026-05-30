from pathlib import Path

def get_project_root() -> Path:
    PROJECT_TOML: str = "pyproject.toml"
    current_dir: Path = Path(__file__).parent
    project_root: Path = current_dir

    while not (project_root / PROJECT_TOML).exists() and project_root != project_root.parent:
        project_root = project_root.parent

    if not (project_root / PROJECT_TOML).exists():
        raise FileNotFoundError(f"Could not find project root with {PROJECT_TOML}")

    return project_root
