import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  bvwbjplbgvbhsrlpgdmjqwftvncz
   ^  ^
  {b: 1, v: 1, w: 1, j: 1}
  """
  datastream_buffer = data[0].rstrip()
  num_unique = 4
  left_ptr, right_ptr = 0, num_unique - 1
  seen = {}
  for i in range(num_unique):
        seen[datastream_buffer[i]] = seen.get(datastream_buffer[i], 0) + 1
  while right_ptr < len(datastream_buffer):
        if len(seen) == num_unique:
            return right_ptr + 1
        seen[datastream_buffer[left_ptr]] -= 1
        if seen[datastream_buffer[left_ptr]] == 0: del seen[datastream_buffer[left_ptr]]
        left_ptr += 1
        right_ptr += 1
        seen[datastream_buffer[right_ptr]] = seen.get(datastream_buffer[right_ptr], 0) + 1
  return -1

def part_2(data: list[str]) -> int:
  """
  part 2
  """
  datastream_buffer = data[0].rstrip()
  num_unique = 14
  left_ptr, right_ptr = 0, num_unique - 1
  while right_ptr < len(datastream_buffer):
        unique = len(set(datastream_buffer[left_ptr:right_ptr+1]))
        if num_unique == unique:
            return right_ptr + 1
        left_ptr += 1
        right_ptr += 1
  return -1
  # datastream_buffer = data[0].rstrip()
  # num_unique = 14
  # left_ptr, right_ptr = 0, num_unique - 1
  # seen = {}
  # for i in range(num_unique):
  #       seen[datastream_buffer[i]] = seen.get(datastream_buffer[i], 0) + 1
  # while right_ptr < len(datastream_buffer):
  #       if len(seen) == num_unique:
  #           return right_ptr + 1
  #       seen[datastream_buffer[left_ptr]] -= 1
  #       if seen[datastream_buffer[left_ptr]] == 0: del seen[datastream_buffer[left_ptr]]
  #       left_ptr += 1
  #       right_ptr += 1
  #       seen[datastream_buffer[right_ptr]] = seen.get(datastream_buffer[right_ptr], 0) + 1
  # return -1
