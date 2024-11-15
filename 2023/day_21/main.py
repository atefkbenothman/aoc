import logging
logger = logging.getLogger()


def print_graph(data: list[str]):
  for line in data:
    logger.debug("".join(line))
  return


def part_1(data: list) -> int:
  """
  part 1
  """
  ROWS = len(data)
  COLS = len(data[0])
  TOTAL_STEPS = 64
  # create debug graph
  debug_graph = []
  for line in data:
    debug_graph.append([i for i in line])
  # get start point
  start_row, start_col = (0, 0)
  for row in range(ROWS):
    for col in range(COLS):
      if data[row][col] == "S":
        start_row, start_col = (row, col)
  # dfs
  directions = [(-1,0),(1,0),(0,1),(0,-1)]
  last = set()
  def dfs(coord: tuple[int, int], visited: set, steps: int):
    nonlocal last
    curr_row, curr_col = coord
    if curr_row not in range(ROWS) or curr_col not in range(COLS):
      return
    if data[curr_row][curr_col] not in [".", "S"]:
      return
    if steps == 0:
      debug_graph[curr_row][curr_col] = "X"
      last.add((curr_row, curr_col))
      return
    for dir_row, dir_col in directions:
      next_row, next_col = curr_row + dir_row, curr_col + dir_col
      dfs((next_row, next_col), visited, steps-1)
    return
  dfs((start_row, start_col), set(), TOTAL_STEPS)
  return len(last)


def part_2(data: list) -> int:
  """
  part 2
  """
  return -1