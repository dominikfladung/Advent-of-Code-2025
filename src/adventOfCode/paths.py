from pathlib import Path

project_root_dir = Path(__file__).parent.parent.parent.absolute()

INPUTS_DIR = project_root_dir / "inputs"
TEMPLATE_PATH = project_root_dir / "templates" / "template.ipynb"
PUZZLES_DIR = project_root_dir / "puzzles"