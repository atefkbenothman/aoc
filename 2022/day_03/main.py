import string
import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)
  result = 0
  for line in data:
        mid = int(len(line) / 2)
        first_sack, second_sack = set(line[:mid]), set(line[mid:])
        appears_in_both = first_sack.intersection(second_sack)
        assert len(appears_in_both) == 1
        result += priority.index(list(appears_in_both)[0]) + 1
  return result


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)
  result = 0
  sacks = []
  for n, line in enumerate(data):
        sacks.append(set(line))
        if ((n + 1) % 3) == 0:
            common_item = sacks[0] & sacks[1] & sacks[2]
            assert len(common_item) == 1
            result += priority.index(list(common_item)[0]) + 1
            sacks = []
  return result
