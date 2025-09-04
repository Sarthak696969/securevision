from typing import Dict, Callable, Any
import torch.nn as nn
from .utils import simple_resnet18

_CREATORS: Dict[str, Callable[..., nn.Module]] = {}

def register(name: str):
    def deco(fn):
        _CREATORS[name]=fn
        return fn
    return deco

def create_model(arch: str, **kwargs) -> nn.Module:
    if arch == "resnet18":
        return simple_resnet18(num_classes=kwargs.get("num_classes",5))
    raise KeyError(f"Unknown arch {arch}")
