import matplotlib.pyplot as plt
from collections import namedtuple

import sudoku

EASY_9X9 = 'sudoku_9x9_easy.txt.txt'
MEDIUM_9X9 = 'sudoku_9x9_medium.txt'
DIFFICULT_9X9 = 'sudoku_9x9_difficult.txt'

EASY_16X16 = 'sudoku_16x16_easy.txt'
MEDIUM_16X16 = 'sudoku_16x16_medium.txt'

EASY_25X25 = 'sudoku_25x25_easy.txt'

ARGS = namedtuple('args', 'games_file board_size agent')


class PerformanceAnalyzer:

    @staticmethod
    def get_running_time(agent, board_size):
        return [
            sudoku.main(args=ARGS(games_file=EASY_9X9, board_size=board_size, agent=agent)),
            sudoku.main(args=ARGS(games_file=MEDIUM_9X9, board_size=board_size, agent=agent)),
            sudoku.main(args=ARGS(games_file=DIFFICULT_9X9, board_size=board_size, agent=agent))
        ]

    def plot_9x9(self):
        x = [1, 2, 3]
        regular_backtracking_running_time = self.get_running_time(agent='BacktrackingAgent', board_size=9)
        csp_backtracking_running_time = self.get_running_time(agent='CspAgent', board_size=9)
        plt.plot(x, regular_backtracking_running_time, '--o', label='Regular Backtracking Agent')
        plt.plot(x, csp_backtracking_running_time, '--o', label='CSP Agent')
        plt.xticks(x, ['easy', 'medium', 'difficult'])
        plt.title('Solving Sudoku 9x9 performance')
        plt.xlabel('difficulty level')
        plt.ylabel('running time (seconds)')
        plt.legend()
        plt.show()


def main():
    performance_analyzer = PerformanceAnalyzer()
    performance_analyzer.plot_9x9()


if __name__ == '__main__':
    main()
