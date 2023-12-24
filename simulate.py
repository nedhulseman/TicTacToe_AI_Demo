import typer
import pandas as pd
from TicTacToe import Manager


def simulate(num_sims=1000):
    tracker = pd.DataFrame(columns=["Game", "Winner"]+list(range(0, 9)))
    tensor_wins = 0
    for i in range(num_sims):
        manager = Manager(X="TensorBot", O="RandBot")
        board, winner = manager.play_game(verbose=False)
        game = pd.DataFrame(board, columns=list(range(0, 9)))
        game["Winner"] = winner
        game["Game"] = i
        tracker = pd.concat([tracker, game], axis=0)
        if winner == "X":
            tensor_wins += 1
    print(tensor_wins)
    #tracker.to_csv("./Data/Simulations_TB_1000_w_Random.csv", index=False)
if __name__ == "__main__":
    typer.run(simulate)