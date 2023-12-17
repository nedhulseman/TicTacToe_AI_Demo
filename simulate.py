import typer
import pandas as pd
from TicTacToe import Manager


def simulate(num_sims=100):
    tracker = pd.DataFrame(columns=["Game", "Winner"]+list(range(0, 9)))
    for i in range(num_sims):
        manager = Manager(X="RandBot", O="RandBot")
        board, winner = manager.play_game()
        game = pd.DataFrame(board, columns=list(range(0, 9)))
        game["Winner"] = winner
        game["Game"] = i
        tracker = pd.concat([tracker, game], axis=0)
    tracker.to_csv("Simulations.csv")
if __name__ == "__main__":
    typer.run(simulate)