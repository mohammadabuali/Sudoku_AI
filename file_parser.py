import xlrd
import numpy as np


def read_games(games_file):
    f = open(games_file, "r")
    game_string = f.read()

    games = game_string.split("\n\n")

    # final games holds a list of list where each list is a separate string representation of the game
    final_games = [[character.strip() for line in games[i].split("\n") for character in line.split()]
                   for i in range(len(games))]

    # print(final_games)
    return final_games


def read_excel_sheets(games_file):
    final_games = []
    workbook = xlrd.open_workbook(games_file)
    f = open('sudoku_9x9_extreme.txt', 'w+')

    for i in range(workbook.nsheets):
        sheet = workbook.sheet_by_index(i)
        for i in range(1, sheet.nrows, 1):
            for character in convert_blanks_in_row_to_zeros(sheet.row_values(i)).split():

                f.write(character + " ")
            f.write("\n") # end of the line
        f.write("\n") # end of an individual game
    # print(final_games)

    f.close()
    # return final_games


def convert_game(sheet):
    game_string = ""
    for i in range(1, sheet.nrows, 1):
        game_string += convert_blanks_in_row_to_zeros(sheet.row_values(i))
    return game_string.split()


def convert_blanks_in_row_to_zeros(row):
    print("Row")
    print(row)
    string = ""
    for val in row:
        if val == '':
            string += " 0 "
        else:
            string += (" " + str(int(val)) + " ")

    print(string)
    return string
