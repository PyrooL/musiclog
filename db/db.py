import json
from pathlib import Path
import importlib.util
from core.models import Album

DEFAULT_COLLECTION_PATH = Path("collection.json") # read from settings.py?

def get_collection_path():
    settings_path = Path("config/settings.py")
    if settings_path.exists():
        try:
            spec = importlib.util.spec_from_file_location("settings", settings_path)
            settings = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(settings)
            return Path(settings.COLLECTION_FILE)
        except AttributeError:
            print(f"Warning: 'COLLECTION_FILE' not found in config/settings.py. Using default: {DEFAULT_COLLECTION_PATH}")
        except Exception as e:
            print(f"Warning: Error loading config/settings.py: {e}. Using default: {DEFAULT_COLLECTION_PATH}")
    else:
        print(f"Warning: config/settings.py not found. Using default: {DEFAULT_COLLECTION_PATH}")

    return DEFAULT_COLLECTION_PATH

COLLECTION_PATH = get_collection_path()
print(f"Loaded collection from {COLLECTION_PATH}")

def load_collection():
    if COLLECTION_PATH.exists():
        try:
            with open(COLLECTION_PATH, "r", encoding="utf-8") as f:
                if COLLECTION_PATH.stat().st_size == 0:
                    return []
                raw = json.load(f)
                return [Album(**data) for data in raw]
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in {COLLECTION_PATH}: {e}")
            return []

    print("File not found: collection.json")
    return []

def save_collection(collection):
    with open(COLLECTION_PATH, "w", encoding="utf-8") as f:
        json.dump([album.__dict__ for album in collection], f, indent=2)
