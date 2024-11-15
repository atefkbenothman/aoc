import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  result = 0
  for line in data:
        first, second = line.split(",")
        first_start, first_end = int(first.split("-")[0]), int(first.split("-")[1])
        second_start, second_end = int(second.split("-")[0]), int(second.split("-")[1])
        if (first_start >= second_start) and (first_end <= second_end):
            result += 1
        elif (first_start <= second_start) and (first_end >= second_end):
            result += 1
  return result


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  result = 0
  for line in data:
        first, second = line.split(",")
        first_start, first_end = int(first.split("-")[0]), int(first.split("-")[1])
        second_start, second_end = int(second.split("-")[0]), int(second.split("-")[1])
        if (second_start >= first_start) and (second_start <= first_end):
            result += 1
        elif (second_end >= first_start) and (second_end <= first_end):
            result += 1
        elif (first_start >= second_start) and (first_end <= second_end):
            result += 1
  return result
