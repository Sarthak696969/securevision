# Placeholder: In production, implement real FF++ downloader & frame extractor.
# For tests, we generate a tiny synthetic 'ffpp' directory with two classes: real/fake.
import os
from pathlib import Path
import numpy as np
from PIL import Image

def synth(root="data/ffpp", n=40):
    root = Path(root)
    for split in ["train","val","test"]:
        for cls in ["real","fake"]:
            (root/split/cls).mkdir(parents=True, exist_ok=True)
            for i in range(n//4 if split=="train" else n//8):
                arr = (np.random.rand(64,64,3)*255).astype("uint8")
                Image.fromarray(arr).save(root/split/cls/f"{i}.png")
    print("Synthetic FF++ dataset created at", root)

if __name__=="__main__":
    synth()
