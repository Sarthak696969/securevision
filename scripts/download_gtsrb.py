import os, tarfile, hashlib, urllib.request, sys, pathlib, zipfile
from pathlib import Path

# To keep repo light, create a tiny synthetic GTSRB-like dataset (32x32 RGB) for smoke tests.
def _synth(dst: Path, n_classes=5, n=200):
    import numpy as np, PIL.Image as Image, random
    rng = np.random.default_rng(0)
    for split in ["train","val","test"]:
        for c in range(n_classes):
            (dst / split / str(c)).mkdir(parents=True, exist_ok=True)
            k = n//10 if split!="train" else n//5
            for i in range(k):
                img = (rng.random((32,32,3))*255).astype("uint8")
                Image.fromarray(img).save(dst / split / str(c) / f"{i}.png")

def main(root="data/gtsrb"):
    dst = Path(root)
    if dst.exists() and any(dst.iterdir()):
        print("Dataset already exists:", dst)
        return
    _synth(dst)
    print("Synthetic GTSRB written to", dst)

if __name__ == "__main__":
    main()
