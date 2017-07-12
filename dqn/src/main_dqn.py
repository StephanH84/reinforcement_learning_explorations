from q_learning.src.game import TicTacToe, RunRL
from q_learning.src.q_learning_agent import Agent as PreciseAgent
from agent import Agent


def main():
    game = TicTacToe()
    alpha = 1e-4
    gamma = 0.5
    agentA = Agent(game, alpha, gamma)
    agentB = PreciseAgent(game, alpha, gamma=0.7)
    runGame = RunRL(game, agentA, agentB)

    runGame.run(episodes=250)

main()