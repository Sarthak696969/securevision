import torch
from securevision.models.registry import create_model
from securevision.attacks.fgsm import fgsm

def test_fgsm_shape():
    model = create_model("resnet18", num_classes=5)
    x = torch.rand(2,3,32,32)
    y = torch.tensor([1,2])
    x_adv = fgsm(model, x, y, 0.01)
    assert x_adv.shape == x.shape
