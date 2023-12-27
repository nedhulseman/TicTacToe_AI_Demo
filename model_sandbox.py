
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

model = torch.load("./Models/Gen4.pt")

moves = [
    [ 1, 0,-1,  1,-1, -1,-1,0, 1],
    [-1, 0, 1, -1, 1,  1, 1,0,-1]

]
with torch.no_grad():
    _X =  torch.tensor([moves], dtype=torch.float32)
    y_pred = model(_X)
    print(y_pred)