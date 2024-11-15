import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> str:
  """
  part 1
  """
  COLS = 9
  drawings, instructions = data[:data.index("\n")][:-1], data[data.index("\n") + 1:]
  cargo = {}
  for line in drawings:
        idx = 1
        rows = []
        for i in range(COLS):
            rows.append(line[idx])
            idx += 4
        for i in range(COLS):
            if rows[i] != " ":
                if (i + 1) in cargo:
                    cargo[i + 1].append(rows[i])
                else:
                    cargo[i + 1] = [rows[i]]
  for inst in instructions:
        instruction = inst.rstrip().split()
        quantity, source, target = int(instruction[1]), int(instruction[3]), int(instruction[5])
        for _ in range(quantity):
            val = cargo[source].pop(0)
            cargo[target].insert(0, val)
  result = ""
  for i in range(COLS):
        result += cargo[i + 1][0]
  return result


def part_2(data: list[str]) -> str:
  """
  part 2
  """
  COLS = 9
  drawings, instructions = data[:data.index("\n")][:-1], data[data.index("\n") + 1:]
  cargo = {}
  for line in drawings:
        idx = 1
        rows = []
        for i in range(COLS):
            rows.append(line[idx])
            idx += 4
        for i in range(COLS):
            if rows[i] != " ":
                if (i + 1) in cargo:
                    cargo[i + 1].append(rows[i])
                else:
                    cargo[i + 1] = [rows[i]]
  for inst in instructions:
        instruction = inst.rstrip().split()
        quantity, source, target = int(instruction[1]), int(instruction[3]), int(instruction[5])
        crates_to_move = []
        for _ in range(quantity):
            val = cargo[source].pop(0)
            crates_to_move.insert(0, val)
        for crate in crates_to_move:
            cargo[target].insert(0, crate)
  result = ""
  for i in range(COLS):
        result += cargo[i + 1][0]
  return result
