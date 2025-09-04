from securevision.utils.seeds import set_deterministic
from securevision.models.registry import create_model
from securevision.data.loaders.gtsrb import TinyGTSRBDataset
import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import DataLoader

def train_resnet18_tiny(epochs=1, batch_size=16, lr=1e-3, seed=42):
    set_deterministic(seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = create_model("resnet18", num_classes=5).to(device)
    train_ds = TinyGTSRBDataset(split="train")
    val_ds = TinyGTSRBDataset(split="val")
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size)
    opt = optim.Adam(model.parameters(), lr=lr)
    crit = nn.CrossEntropyLoss()
    for epoch in range(epochs):
        model.train()
        for x,y in train_loader:
            x,y = x.to(device), y.to(device)
            opt.zero_grad()
            out = model(x)
            loss = crit(out,y)
            loss.backward(); opt.step()
    # simple eval
    model.eval(); correct=0; total=0
    with torch.no_grad():
        for x,y in val_loader:
            x,y=x.to(device),y.to(device)
            pred = model(x).argmax(dim=1)
            correct += (pred==y).sum().item()
            total += y.numel()
    acc = correct/total if total else 0.0
    return {"val_acc":acc}
