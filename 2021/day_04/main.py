import logging
from collections import defaultdict

logger = logging.getLogger()

def part_1(data: list[str]) -> int:
  numbers_to_draw, board_data = [int(x) for x in data[0].split(",")], data[2:]
  boards = defaultdict(list)
  board_count = 0
  for line in board_data:
    if line == "":
      board_count += 1
      continue
    else:
      row = [int(x) for x in line.split(" ") if x != ""]
      boards[board_count].append(row)

  def check_board_status(board):
    ROWS, COLS = len(board), len(board[0])
    # check horizontal
    for row in range(ROWS):
      found_winner = True
      for col in range(COLS):
        if board[row][col] != "#":
          found_winner = False
          break
      if found_winner:
        return True
    # check vertical
    for col in range(COLS):
      found_winner = True
      for row in range(ROWS):
        if board[row][col] != "#":
          found_winner = False
          break
      if found_winner:
        return True

  for num in numbers_to_draw:
    for board_num, board in boards.items():
      for row in board:
        for col in range(len(row)):
          if row[col] == num:
            row[col] = "#"
          if check_board_status(board):
            # for line in board:
            #   print(line, num)
            result = 0
            for line in board:
              for val in line:
                if val != "#":
                  result += val
            return num * result


def part_2(data: list[str]) -> int:
  numbers_to_draw, board_data = [int(x) for x in data[0].split(",")], data[2:]
  boards = defaultdict(list)
  board_count = 0
  for line in board_data:
    if line == "":
      board_count += 1
      continue
    else:
      row = [int(x) for x in line.split(" ") if x != ""]
      boards[board_count].append(row)

  def check_board_status(board):
    ROWS, COLS = len(board), len(board[0])
    # check horizontal
    for row in range(ROWS):
      found_winner = True
      for col in range(COLS):
        if board[row][col] != "#":
          found_winner = False
          break
      if found_winner:
        return True
    # check vertical
    for col in range(COLS):
      found_winner = True
      for row in range(ROWS):
        if board[row][col] != "#":
          found_winner = False
          break
      if found_winner:
        return True

  def play_game(boards):
    boards_won = []
    boards_won_with_last_num = []
    for num in numbers_to_draw:
      for board_num, board in boards.items():
        for row in board:
          for col in range(len(row)):
            if row[col] == num:
              row[col] = "#"
            if check_board_status(board):
              if board_num not in boards_won:
                boards_won.append(board_num)
                boards_won_with_last_num.append((board_num, num))
              if len(boards_won) == len(boards):
                return boards_won, boards_won_with_last_num, num
              break

  boards_won, boards_won_with_last_num, num = play_game(boards)
  multiplier = boards_won_with_last_num[-1][1]
  result = 0
  for line in boards[boards_won_with_last_num[-1][0]]:
    for val in line:
      if val != "#":
        result += val
  return multiplier * result
