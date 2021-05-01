import torch
from torchvision import models
device = "cuda"
model = models.inception_v3(pretrained=True).to(device)

