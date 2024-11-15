import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  FILE_TREE = {}
  curr_dir = [] # stack
  for line in data:
    line = line.rstrip()
    # command
    if line[0] == "$":
      # cd
      if line.split()[1] == "cd":
        directory = line.split()[2]
        # cd ..
        if directory == "..":
          curr_dir.pop(-1)
        # cd [dir]
        else:
          directory = "/" + directory
          full_directory = curr_dir[-1] + directory if curr_dir else directory
          curr_dir.append(full_directory)
          FILE_TREE[full_directory] = []
    # entries in directory
    else:
      # directory
      if line.split()[0] == "dir":
        directory = "/" + line.split()[1]
        full_directory = curr_dir[-1] + directory
        FILE_TREE[curr_dir[-1]].append(f"dir {full_directory}")
      # normal files
      else:
        FILE_TREE[curr_dir[-1]].append(line)

  result = 0
  def calculate_directory_size(directory_name: str):
    nonlocal result
    entries = FILE_TREE[directory_name]
    total_size = 0
    for entry in entries:
      if entry.split()[0] == "dir":
        dir_name = entry.split()[1]
        total_size += calculate_directory_size(dir_name)
      else:
        file, size = entry.split()[1], int(entry.split()[0])
        total_size += size
    if total_size <= 100_000:
      result += total_size
    return total_size

  first_dir = list(FILE_TREE.keys())[0]
  calculate_directory_size(first_dir)

  return result


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  FILE_TREE = {}
  curr_dir = [] # stack
  for line in data:
    line = line.rstrip()
    # command
    if line[0] == "$":
      # cd
      if line.split()[1] == "cd":
        directory = line.split()[2]
        # cd ..
        if directory == "..":
          curr_dir.pop(-1)
        # cd [dir]
        else:
          directory = "/" + directory
          full_directory = curr_dir[-1] + directory if curr_dir else directory
          curr_dir.append(full_directory)
          FILE_TREE[full_directory] = []
    # entries in directory
    else:
      # directory
      if line.split()[0] == "dir":
        directory = "/" + line.split()[1]
        full_directory = curr_dir[-1] + directory
        FILE_TREE[curr_dir[-1]].append(f"dir {full_directory}")
      # normal files
      else:
        FILE_TREE[curr_dir[-1]].append(line)

  TOTAL_DISK_SPACE_AVAILABLE = 70000000 
  TOTAL_DISK_SPACE_REQUIRED = 30000000

  DIRECTORY_SIZES = []

  def calculate_directory_size(directory_name: str):
    entries = FILE_TREE[directory_name]
    total_size = 0
    for entry in entries:
      if entry.split()[0] == "dir":
        dir_name = entry.split()[1]
        total_size += calculate_directory_size(dir_name)
      else:
        file, size = entry.split()[1], int(entry.split()[0])
        total_size += size
    DIRECTORY_SIZES.append(total_size)
    return total_size

  first_dir = list(FILE_TREE.keys())[0]
  total = calculate_directory_size(first_dir)

  UNUSED_SPACE = TOTAL_DISK_SPACE_AVAILABLE - total
  SPACE_WE_NEED_TO_DELETE = TOTAL_DISK_SPACE_REQUIRED - UNUSED_SPACE

  sorted_directory_sizes = sorted(DIRECTORY_SIZES)

  for size in sorted_directory_sizes:
    if size >= SPACE_WE_NEED_TO_DELETE:
      return size
