import torch.nn as nn
import torch

# A very small ResNet-ish model for smoke tests (lighter than torchvision)
class TinyBlock(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.conv1 = nn.Conv2d(c, c, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(c)
        self.conv2 = nn.Conv2d(c, c, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(c)

    def forward(self, x):
        identity = x
        x = torch.relu(self.bn1(self.conv1(x)))
        x = self.bn2(self.conv2(x))
        return torch.relu(x + identity)

class TinyResNet(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        self.stem = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
        )
        self.block1 = TinyBlock(32)
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(32, num_classes)

    def forward(self, x):
        x = self.stem(x)
        x = self.block1(x)
        x = self.pool(x).flatten(1)
        return self.fc(x)

def simple_resnet18(num_classes=5):
    return TinyResNet(num_classes=num_classes)
