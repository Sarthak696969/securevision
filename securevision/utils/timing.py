import time
from contextlib import contextmanager

@contextmanager
def timer(name: str):
    t0 = time.time()
    yield
    dt = time.time() - t0
    print(f"{name} took {dt:.3f}s")
