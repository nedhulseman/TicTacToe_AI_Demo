import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


gen1  = pd.read_csv("./Data/Simulations_TB_1000_w_Random.csv")
gen2  = pd.read_csv("./Data/Simulations_TBG1_40000.csv")
gen3  = pd.read_csv("./Data/Simulations_TBG1_TBG2_40000.csv")
human = pd.read_csv("./Data/Simulations_Human.csv")
human_oversampled = pd.DataFrame()
for i in range(0, 1000):
    human_oversampled = pd.concat([human_oversampled, human])
dataset = pd.concat([gen1, gen2])
dataset = pd.concat([dataset, gen3])
dataset = pd.concat([dataset, human_oversampled])

dataset_90 = dataset.copy()
dataset_90["2"] = dataset["0"]
dataset_90["5"] = dataset["1"]
dataset_90["8"] = dataset["2"]
dataset_90["1"] = dataset["3"]
dataset_90["7"] = dataset["5"]
dataset_90["0"] = dataset["6"]
dataset_90["3"] = dataset["7"]
dataset_90["6"] = dataset["8"]
dataset_180 = dataset.copy()
dataset_180["8"] = dataset["0"]
dataset_180["7"] = dataset["1"]
dataset_180["6"] = dataset["2"]
dataset_180["5"] = dataset["3"]
dataset_180["3"] = dataset["5"]
dataset_180["2"] = dataset["6"]
dataset_180["1"] = dataset["7"]
dataset_180["0"] = dataset["8"]
dataset_270 = dataset.copy()
dataset_270["6"] = dataset["0"]
dataset_270["3"] = dataset["1"]
dataset_270["0"] = dataset["2"]
dataset_270["7"] = dataset["3"]
dataset_270["1"] = dataset["5"]
dataset_270["8"] = dataset["6"]
dataset_270["5"] = dataset["7"]
dataset_270["2"] = dataset["8"]
dataset = pd.concat([dataset, dataset_90])
dataset = pd.concat([dataset, dataset_180])
dataset = pd.concat([dataset, dataset_270])

dataset = dataset.sample(frac=0.25, random_state=100)


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
X_Val = X[0:50000]
X = X[50000:]
Y_Val = y[0:50000]
y = y[50000:]


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
optimizer = optim.Adam(model.parameters(), lr=1e-3)


n_epochs = 100
batch_size = 10
loss_train = []
loss_val = []
 
for epoch in range(n_epochs):
    for i in range(0, len(X), batch_size):
        Xbatch = X[i:i+batch_size]
        y_pred = model(Xbatch)
        ybatch = y[i:i+batch_size]
        loss = loss_fn(y_pred, ybatch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    loss = loss_fn(y_pred, ybatch)
    y_pred = model(X_Val)
    loss_v = loss_fn(y_pred, Y_Val)
    loss_train.append(loss)
    loss_val.append(loss_v)
    print(f'Finished epoch {epoch}, latest loss {loss}')

loss_tracker = pd.DataFrame(list(zip(loss_train, loss_val)), columns=["Training Loss", "Validation Loss"])
loss_tracker.to_csv("./Assessment/Loss Tracker G4_1.csv")
torch.save(model, "./Models/Gen4_1.pt")


