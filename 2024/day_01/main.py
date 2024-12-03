import logging
logger = logging.getLogger()

def part_1(data: list[str]) -> int:
  left_nums, right_nums = [], []
  for line in data:
    left, right = line.replace("   ", " ").split(" ")
    left_nums.append(int(left))
    right_nums.append(int(right))
  res = 0
  for left, right in zip(sorted(left_nums), sorted(right_nums)):
    res += abs(left - right)
  return res

def part_2(data: list[str]) -> int:
  left_nums, right_nums = [], {}
  for line in data:
    left, right = line.replace("   ", " ").split(" ")
    left_nums.append(int(left))
    right_nums[int(right)] = right_nums.get(int(right), 0) + 1
  res = 0
  for num in left_nums:
    res += num * right_nums[num] if num in right_nums else 0
  return res
