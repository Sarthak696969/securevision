import torch

def fedavg(updates):
    return sum(updates)/len(updates)

def median(updates):
    return torch.median(torch.stack(updates), dim=0).values

def trimmed_mean(updates, trim_ratio=0.1):
    k = int(len(updates)*trim_ratio)
    stacked = torch.stack(updates)
    sorted_, _ = torch.sort(stacked, dim=0)
    trimmed = sorted_[k:len(updates)-k]
    return trimmed.mean(dim=0)

def krum(updates, num_to_select=1):
    # naive: return first update (placeholder)
    return updates[0]

def fltrust(updates):
    # placeholder: average
    return fedavg(updates)
