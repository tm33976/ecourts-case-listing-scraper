from typing import Dict
import json, os

DATA_DIR = os.path.join(os.getcwd(), "ecourts_data")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    return DATA_DIR

def save_json(obj: Dict, filename: str) -> str:
    ensure_data_dir()
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    return path
