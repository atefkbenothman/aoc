import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  depth = 0
  horizontal_pos = 0
  for line in data:
    cmd, steps = line.split()[0], int(line.split()[1])
    if cmd == "forward":
      horizontal_pos += steps
    elif cmd == "down":
      depth += steps
    elif cmd == "up":
      depth -= steps
  return depth * horizontal_pos


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  depth = 0
  horizontal_pos = 0
  aim = 0
  for line in data:
    cmd, steps = line.split()[0], int(line.split()[1])
    if cmd == "forward":
      horizontal_pos += steps
      depth += aim * steps
    elif cmd == "down":
      aim += steps
    elif cmd == "up":
      aim -= steps
  return depth * horizontal_pos
