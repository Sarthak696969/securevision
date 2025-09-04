import torch
from securevision.evaluation.metrics import accuracy

def test_accuracy():
    preds = torch.tensor([[0.1,0.9],[0.8,0.2]])
    labels = torch.tensor([1,0])
    assert accuracy(preds, labels) == 1.0
