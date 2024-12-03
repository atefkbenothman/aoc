import logging
logger = logging.getLogger()

def part_1(data: list[str]) -> int:
  fishes = [int(x) for x in data[0].split(",")]
  days = 80
  day = 0
  while day < days:
    for i in range(len(fishes)):
      if fishes[i] == 0:
        fishes[i] = 6
        fishes.append(8)
      else:
        fishes[i] -= 1
    day += 1
  return len(fishes)

def part_2(data: list[str]) -> int:
  num_fish = [0 for _ in range(9)]
  fishes = [int(x) for x in data[0].split(",")]
  for fish in fishes:
    num_fish[fish] += 1
  for _ in range(256):
    fish_to_add = 0
    for i in range(len(num_fish)):
      if i == 8:
        num_fish[i] = fish_to_add
        continue
      if i == 0:
        fish_to_add = num_fish[0]
        num_fish[7] += fish_to_add
      num_fish[i] = num_fish[i + 1]
  return sum(num_fish)
