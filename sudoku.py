import argparse
from datetime import datetime

from backtracking_agent import BacktrackingAgent
from simulated_annealing_agent import SA_Agent
from stochastic_beam_search import SBS_Agent
from csp_agent import CspAgent, CspHeuristic
from board import Board
import file_parser


class GameRunner:
    def __init__(self, agent, board):
        self.agent = agent
        self.board = board

    def run(self):
        start = datetime.now()
        if self.agent.solve():
            assert self.board.win()
            print(self.board)
        else:
            assert not self.board.win()
            print('board can not be solved!')
        print(datetime.now() - start)


def create_agent(agent, board, temp, decay, iterations):
    if agent == 'BacktrackingAgent':
        return BacktrackingAgent(board)
    elif agent == 'CspAgent':
        return CspAgent(board, CspHeuristic.MRV, CspHeuristic.LCV)
    elif agent == 'SA_Agent':
        return SA_Agent(board, temp, decay)
    elif agent == 'SBS_Agent':
        return SBS_Agent(board, iterations)


def main(args):
    start = datetime.now()
    games = file_parser.read_games(args.games_file)  # file_parser.read_excel_sheets(args.games_file)
    for entries in games:
        board = Board(entries, args.board_size)
        agent = create_agent(args.agent, board, args.temp, args.decay, args.iterations)
        game_runner = GameRunner(agent, board)
        game_runner.run()

    duration = datetime.now() - start
    average_running_time = duration/len(games)
    print("end time: " + str(duration))
    print(f"average running time: {average_running_time}")

    return average_running_time.total_seconds()


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Sudoku game.')
    args_parser.add_argument('--games_file', help='file of Sudoku boards.', type=str)
    args_parser.add_argument('--board_size', help='The board size.', type=int)
    args_parser.add_argument('--temp', help='The board size.', type=int)
    args_parser.add_argument('--decay', help='The board size.', type=int)
    args_parser.add_argument('--iterations', help='The board size.', type=int)

    # TODO: TBD
    agents = ['BacktrackingAgent', 'CspAgent', 'SA_Agent', 'SBS_Agent']
    args_parser.add_argument('--agent', choices=agents, help='The agent.', default=agents[1], type=str)

    _args = args_parser.parse_args()
    main(_args)
