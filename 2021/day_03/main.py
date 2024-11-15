import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  grid = []
  for line in data:
    grid.append([int(i) for i in line])
  ROWS, COLS = len(grid), len(grid[0])
  gamma_rate, epsilon_rate = "", ""
  for col in range(COLS):
    one_count, zero_count = 0, 0
    row = 0
    while row in range(ROWS):
      if grid[row][col] == 1:
        one_count += 1
      else:
        zero_count += 1
      row += 1
    if one_count > zero_count:
      gamma_rate += "1"
      epsilon_rate += "0"
    else:
      gamma_rate += "0"
      epsilon_rate += "1"
  gamma_rate = int(gamma_rate, 2)
  epsilon_rate = int(epsilon_rate, 2)
  return gamma_rate * epsilon_rate


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  oxygen = [line for line in data]
  co2 = [line for line in data]

  def count_ones_and_zeroes(queue, col):
    ROWS = len(queue)
    one_count, zero_count = 0, 0
    for row in range(ROWS):
      if queue[row][col] == "1":
        one_count += 1
      else:
        zero_count += 1
    return one_count, zero_count

  bit_idx = 0
  while len(oxygen) > 1:
    ones, zeroes = count_ones_and_zeroes(oxygen, bit_idx)
    if ones < zeroes:
      temp = [i for i in oxygen if i[bit_idx] == "0"]
    else:
      temp = [i for i in oxygen if i[bit_idx] == "1"]
    oxygen = temp
    bit_idx += 1

  bit_idx = 0
  while len(co2) > 1:
    ones, zeroes = count_ones_and_zeroes(co2, bit_idx)
    if ones < zeroes:
      temp = [i for i in co2 if i[bit_idx] == "1"]
    else:
      temp = [i for i in co2 if i[bit_idx] == "0"]
    co2 = temp
    bit_idx += 1

  return int(oxygen[0], 2) * int(co2[0], 2)
