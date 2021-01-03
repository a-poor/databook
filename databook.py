"""
databook.py
created by Austin Poor



"""

import json
from pathlib import Path

def initialize():
    home_dir = Path("~/.databook")
    home_dir.mkdir(exist_ok=True)
    (home_dir / "").mkdir(exist_ok=True)

def add_dataset():
    pass

def list_datasets():
    pass

def update_dataset_info():
    pass

if __name__ == "__main__":
    pass
