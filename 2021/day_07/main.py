import logging
logger = logging.getLogger()

def part_1(data: list[str]) -> int:
  data = [int(x) for x in data[0].split(",")]
  # brute force
  result = float("inf")
  for num1 in data:
    s = 0
    for num2 in data:
      s += abs(num1 - num2)
    result = min(result, s)
  return result

def part_2(data: list[str]) -> int:
  return -1
