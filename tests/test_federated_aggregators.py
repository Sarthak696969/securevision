import torch
from securevision.federated.aggregators import fedavg, median, trimmed_mean

def test_fedavg():
    us = [torch.ones(3), 2*torch.ones(3)]
    out = fedavg(us)
    assert torch.allclose(out, 1.5*torch.ones(3))

def test_median():
    us = [torch.tensor([0.,10.,2.]), torch.tensor([1.,3.,2.]), torch.tensor([2.,4.,2.])]
    out = median(us)
    assert torch.allclose(out, torch.tensor([1.,4.,2.]))

def test_trimmed():
    us = [torch.zeros(3), torch.ones(3), 10*torch.ones(3)]
    out = trimmed_mean(us, trim_ratio=1/3)
    assert torch.allclose(out, torch.ones(3))
