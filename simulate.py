import typer
import pandas as pd
from TicTacToe import Manager
from TicTacToe import Player



def simulate(num_sims=1):
    tracker = pd.DataFrame(columns=["Game", "Winner"]+list(range(0, 9)))
    tensor_wins = 0
    for i in range(num_sims):
        manager = Manager(X=Player("TensorBot", side="X", bot_gen="Gen4_1", mutation=False), O=Player("TensorBot", side="O", bot_gen="Gen4", mutation=False))
        #manager = Manager(X=Player("TensorBot", side="X", bot_gen="Gen4_1", mutation=False), O=Player("Human", side="O"))
        #manager = Manager(X=Player("Human", side="x"), O=Player("TensorBot", side="O", bot_gen="Gen4", mutation=False))
        #manager = Manager(X=Player("TensorBot", side="X", bot_gen="Gen4_1", mutation=False), O=Player("RandBot", side="O"))
        board, winner = manager.play_game(verbose=True)
        game = pd.DataFrame(board, columns=list(range(0, 9)))
        game["Winner"] = winner
        game["Game"] = i
        tracker = pd.concat([tracker, game], axis=0)
        if winner == "X":
            tensor_wins += 1
    print(tensor_wins)
    #tracker.to_csv("./Data/Simulations_TBG1_TBG2_40000.csv", index=False)
if __name__ == "__main__":
    typer.run(simulate)