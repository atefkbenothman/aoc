import logging
from collections import defaultdict

logger = logging.getLogger()

def part_1(data: list[str]) -> int:
  positions = defaultdict(int)
  for d in data:
    pos_1, pos_2 = d.replace(" ", "").split("->")
    pos_1_x, pos_1_y = [int(i) for i in pos_1.split(",")]
    pos_2_x, pos_2_y = [int(i) for i in pos_2.split(",")]
    if pos_1_y == pos_2_y:
      diff = abs(pos_1_x - pos_2_x)
      for i in range(diff + 1):
        if pos_1_x > pos_2_x:
          positions[(pos_1_x - i, pos_1_y)] += 1
        else:
          positions[(pos_1_x + i, pos_1_y)] += 1
    elif pos_1_x == pos_2_x:
      diff = abs(pos_1_y - pos_2_y)
      for i in range(diff + 1):
        if pos_1_y > pos_2_y:
          positions[(pos_1_x, pos_1_y - i)] += 1
        else:
          positions[(pos_1_x, pos_1_y + i)] += 1
  return sum([1 for pos, count in positions.items() if count > 1])

def part_2(data: list[str]) -> int:
  positions = defaultdict(int)
  for d in data:
    pos_1, pos_2 = d.replace(" ", "").split("->")
    pos_1_x, pos_1_y = [int(i) for i in pos_1.split(",")]
    pos_2_x, pos_2_y = [int(i) for i in pos_2.split(",")]
    if pos_1_y == pos_2_y:
      diff = abs(pos_1_x - pos_2_x)
      for i in range(diff + 1):
        if pos_1_x > pos_2_x:
          positions[(pos_1_x - i, pos_1_y)] += 1
        else:
          positions[(pos_1_x + i, pos_1_y)] += 1
    elif pos_1_x == pos_2_x:
      diff = abs(pos_1_y - pos_2_y)
      for i in range(diff + 1):
        if pos_1_y > pos_2_y:
          positions[(pos_1_x, pos_1_y - i)] += 1
        else:
          positions[(pos_1_x, pos_1_y + i)] += 1
    else:
      if pos_1_x > pos_2_x:
        if pos_1_y > pos_2_y:
          # go left,up: 3,3 -> 1,1
          diff = abs(pos_1_x - pos_2_x)
          for i in range(diff + 1):
            positions[(pos_1_x - i, pos_1_y - i)] += 1
        else:
          # go left,down: 3,3 -> 1,5
          diff = abs(pos_1_x - pos_2_x)
          for i in range(diff + 1):
            positions[(pos_1_x - i, pos_1_y + i)] += 1
      else:
        if pos_1_y > pos_2_y:
          # go right,up: 3,3 -> 5,1
          diff = abs(pos_1_y - pos_2_y)
          for i in range(diff + 1):
            positions[(pos_1_x + i, pos_1_y - i)] += 1
        else:
          # go right,down: 3,3 -> 5,5
          diff = abs(pos_1_y - pos_2_y)
          for i in range(diff + 1):
            positions[(pos_1_x + i, pos_1_y + i)] += 1
  return sum([1 for pos, count in positions.items() if count > 1])
