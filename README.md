# Basic Demonstration of PyTorch for Tic Tac Toe
## Approach for Data Generation
1. Play ~20,000 tic tac toe games using RandomBot engine, Play ~20 human games against RandomBot and oversample to train `TensorBotGen1`
2. TensorBotG1 plays ~40,000 games against RandomBot to train `TensorBotGen2`
3. TensorBotG2 plays TensorBotG1 for ~40,000 games to train `TensorBotGen3`
4. `TensorBotGen4` is trained on all cumulative data
5. `TensorBotGen4.1` rotates the cumulative matrices 90&deg;, 180&deg; & 270&deg;. Then re-samples 25% of the data

## Results
The performance against a RandomBot in Tic Tac Toe improves with each subsequent generation of TensorBot with the final version winning about 99.9% of games against a RandomBot.
![alt text](https://github.com/nedhulseman/TicTacToe_AI_Demo/edit/main/Win_Dists.png?raw=true)

