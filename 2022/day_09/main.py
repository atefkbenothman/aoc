import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  DIRECTIONS = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}
  VISITED = set()

  HEAD_POS_ROW = 0
  HEAD_POS_COL = 0
  TAIL_POS_ROW = 0
  TAIL_POS_COL = 0
  HEAD_POS = (HEAD_POS_ROW, HEAD_POS_COL)
  TAIL_POS = (TAIL_POS_ROW, TAIL_POS_COL)

  VISITED.add(TAIL_POS)

  for line in data:
    direction, steps = line.split()[0], int(line.split()[1])
    dir_row, dir_col = DIRECTIONS[direction]
    for _ in range(steps):
      HEAD_POS_ROW, HEAD_POS_COL = dir_row + HEAD_POS_ROW, dir_col + HEAD_POS_COL
      ROW_DIFF, COL_DIFF = HEAD_POS_ROW - TAIL_POS_ROW, HEAD_POS_COL - TAIL_POS_COL
      if abs(ROW_DIFF) == 2 and COL_DIFF == 0:
        TAIL_POS_ROW += dir_row
      elif abs(ROW_DIFF) == 2 and COL_DIFF == 1:
        TAIL_POS_ROW += dir_row
        TAIL_POS_COL += 1
      elif abs(ROW_DIFF) == 2 and COL_DIFF == -1:
        TAIL_POS_ROW += dir_row
        TAIL_POS_COL -= 1
      elif abs(COL_DIFF) == 2 and ROW_DIFF == 0:
        TAIL_POS_COL += dir_col
      elif abs(COL_DIFF) == 2 and ROW_DIFF == 1:
        TAIL_POS_COL += dir_col
        TAIL_POS_ROW += 1
      elif abs(COL_DIFF) == 2 and ROW_DIFF == -1:
        TAIL_POS_COL += dir_col
        TAIL_POS_ROW -= 1
      VISITED.add((TAIL_POS_ROW, TAIL_POS_COL))
      print((HEAD_POS_ROW, HEAD_POS_COL), (TAIL_POS_ROW, TAIL_POS_COL))

  return len(VISITED)


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  DIRECTIONS = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}
  VISITED = set()

  HEAD_POS_ROW, HEAD_POS_COL = 0, 0
  POSITIONS = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

  for line in data:
    direction, steps = line.split()[0], int(line.split()[1])
    dir_row, dir_col = DIRECTIONS[direction]
    for _ in range(steps):
      # move head
      HEAD_POS_ROW, HEAD_POS_COL = HEAD_POS_ROW + dir_row, HEAD_POS_COL + dir_col
      PREV_HEAD_POS_ROW, PREV_HEAD_POS_COL = HEAD_POS_ROW, HEAD_POS_COL
      # move children
      for i in range(len(POSITIONS)):
        ORIG_ROW, ORIG_COL = POSITIONS[i]
        CURR_ROW, CURR_COL = POSITIONS[i]
        ROW_DIFF, COL_DIFF = PREV_HEAD_POS_ROW - CURR_ROW, PREV_HEAD_POS_COL - CURR_COL
        if abs(ROW_DIFF) > 1 or abs(COL_DIFF) > 1:
          CURR_ROW += (1 if ROW_DIFF > 0 else -1 if ROW_DIFF < 0 else 0)
          CURR_COL += (1 if COL_DIFF > 0 else -1 if COL_DIFF < 0 else 0)
        POSITIONS[i] = (CURR_ROW, CURR_COL)
        PREV_HEAD_POS_ROW, PREV_HEAD_POS_COL = CURR_ROW, CURR_COL
        VISITED.add(POSITIONS[8])

  return len(VISITED)
