import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from TicTacToe import Manager
from TicTacToe import Player

num_sims = 100
games = 100
tensor_bots = [["RandBot", ""], ["TensorBot", "Gen1"], ["TensorBot", "Gen2"], ["TensorBot", "Gen3"], ["TensorBot", "Gen4"], ["TensorBot", "Gen4_1"]]
tracker = {}
for bot in tensor_bots:
    tracker["_".join(bot)] = []
    for sim in range(num_sims):
        tensor_wins = 0
        for game in range(games):
            manager = Manager(X=Player(bot[0], side="X", bot_gen=bot[1], mutation=False), O=Player("RandBot", side="O"))
            board, winner = manager.play_game(verbose=False)
            if winner == "X":
                tensor_wins += 1
        tracker["_".join(bot)].append(tensor_wins)
tracker_df = pd.DataFrame(tracker)
tracker_df.to_csv("./Assessment/Simulations.csv", index=False)


ax = sns.kdeplot(tracker_df, fill=True, alpha=.3)\
    .set(
        xlabel="Number of Wins out of 100 Games", 
        ylabel="Density",
        title="Performance of Neural Networks")
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

