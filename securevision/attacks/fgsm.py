import torch

def fgsm(model, x, y, eps=0.031):
    x = x.clone().detach().requires_grad_(True)
    out = model(x)
    loss = torch.nn.functional.cross_entropy(out, y)
    loss.backward()
    x_adv = x + eps * x.grad.sign()
    x_adv = torch.clamp(x_adv, 0, 1)
    return x_adv.detach()
