import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "config.yaml"

class Config:
    def __init__(self, path=CONFIG_PATH):
        with open(path, "r") as f:
            self.cfg = yaml.safe_load(f)
            
    def __getitem__(self, item):
        return self.cfg[item]