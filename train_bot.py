import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

'''
dataset_bot = pd.read_csv("Simulations.csv")
dataset_hum = pd.read_csv("Simulations_Human.csv")
df = pd.concat([dataset_bot, dataset_hum])
for i in range(0, 40):
    dataset = pd.concat([df, dataset_hum])
dataset = dataset.sample(frac=1, random_state=100)
'''
dataset = pd.read_csv("./Data/Simulations_TB_1000_w_Random.csv")
X = dataset[[i for i in dataset.columns if i not in ["Game", "Winner"]]]
X = X.replace("X",1)
X = X.replace("O",-1)
X = X.fillna(0)
y = dataset[["Winner"]].fillna("Split")
y = y.replace("X", 1)
y = y.replace("O", 0)
y = y.replace("Split", 0)

X = torch.tensor(X.to_numpy(), dtype=torch.float32)
y = torch.tensor(y.to_numpy(), dtype=torch.float32).reshape(-1, 1)


model = nn.Sequential(
    nn.Linear(X.shape[1], 12),
    nn.ReLU(),
    nn.Linear(12, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)

print(model)

loss_fn = nn.BCELoss()  # binary cross entropy
optimizer = optim.Adam(model.parameters(), lr=0.001)


n_epochs = 100
batch_size = 10
 
for epoch in range(n_epochs):
    for i in range(0, len(X), batch_size):
        Xbatch = X[i:i+batch_size]
        y_pred = model(Xbatch)
        ybatch = y[i:i+batch_size]
        loss = loss_fn(y_pred, ybatch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'Finished epoch {epoch}, latest loss {loss}')

torch.save(model, "./Models/Gen2.pt")


