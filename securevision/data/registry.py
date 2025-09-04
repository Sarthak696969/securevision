from typing import Dict, Callable
_REGISTRY: Dict[str, Callable] = {}

def register(name: str):
    def deco(fn):
        _REGISTRY[name]=fn
        return fn
    return deco

def get(name: str):
    return _REGISTRY[name]
