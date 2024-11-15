import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  total_increases = 0
  for i in range(1, len(data)):
    curr_depth, last_depth = int(data[i]), int(data[i-1])
    total_increases += 1 if curr_depth > last_depth else 0
  return total_increases


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  total_increases = 0
  for i in range(len(data) - 3):
    first_window, second_window = data[i:i+3], data[i+1:i+3+1]
    first_window_size, second_window_size = sum([int(i) for i in first_window]), sum([int(i) for i in second_window])
    total_increases += 1 if second_window_size > first_window_size else 0
  return total_increases
