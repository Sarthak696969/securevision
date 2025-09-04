import torch
from torch.utils.data import Dataset
from PIL import Image
from pathlib import Path
import numpy as np

ROOT = Path("data/gtsrb")

class TinyGTSRBDataset(Dataset):
    def __init__(self, split="train", n_classes=5):
        self.paths = []
        base = ROOT / split
        for c in range(n_classes):
            cls_dir = base/str(c)
            if not cls_dir.exists():
                continue
            for p in cls_dir.glob("*.png"):
                self.paths.append((p,c))
        if not self.paths:
            # try to generate synthetic via script if missing
            from subprocess import run
            run(["python","scripts/download_gtsrb.py"], check=True)
            for c in range(n_classes):
                for p in (ROOT/split/str(c)).glob("*.png"):
                    self.paths.append((p,c))

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        p,c = self.paths[idx]
        img = Image.open(p).convert("RGB").resize((32,32))
        arr = np.array(img).astype("float32")/255.0
        arr = torch.from_numpy(arr).permute(2,0,1)
        return arr, torch.tensor(c, dtype=torch.long)
