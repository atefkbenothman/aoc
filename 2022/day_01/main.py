import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  max_calories = 0
  total_calories = 0
  for line in data:
        if line:
            total_calories += int(line)
        else:
            max_calories = max(max_calories, total_calories)
            total_calories = 0
  if total_calories > 0:
      max_calories = max(max_calories, total_calories)
  return max_calories


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  result = []
  total_calories = 0
  for line in data:
        if line:
            total_calories += int(line)
        else:
            result.append(total_calories)
            total_calories = 0
  if total_calories > 0:
      result.append(total_calories)
  return sum(sorted(result, reverse=True)[:3])
