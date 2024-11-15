import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  ROWS, COLS = len(data), len(data[0])

  def check_dir(row: int, col: int, row_diff: int, col_diff: int):
    orig_val = data[row][col]
    row += row_diff
    col += col_diff
    while row in range(ROWS) and col in range(COLS):
      if data[row][col] >= orig_val:
        return False
      row += row_diff
      col += col_diff
    return True

  count = 0
  for row in range(1, ROWS - 1):
    for col in range(1, COLS - 1):
      is_visible = (
        check_dir(row, col, 1, 0) or
        check_dir(row, col, -1, 0) or
        check_dir(row, col, 0, 1) or
        check_dir(row, col, 0, -1)
      )
      if is_visible: count += 1

  trees_on_edge = (ROWS * COLS) - ((ROWS - 2) * (COLS - 2))
  return count + trees_on_edge


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  ROWS, COLS = len(data), len(data[0])

  def check_dir(row: int, col: int, row_diff: int, col_diff: int):
    orig_val = data[row][col]
    row += row_diff
    col += col_diff
    trees_visible = 0
    while row in range(ROWS) and col in range(COLS):
      if data[row][col] >= orig_val:
        trees_visible += 1
        break
      row += row_diff
      col += col_diff
      trees_visible += 1
    return trees_visible

  max_scenic_score = 0

  for row in range(1, ROWS - 1):
    for col in range(1, COLS - 1):
      scenic_score = (
        check_dir(row, col, 1, 0) *
        check_dir(row, col, -1, 0) *
        check_dir(row, col, 0, 1) *
        check_dir(row, col, 0, -1)
      )
      max_scenic_score = max(max_scenic_score, scenic_score)

  return max_scenic_score
