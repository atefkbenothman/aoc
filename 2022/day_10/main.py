import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  X = 1
  cycles = 0
  result = 0
  for line in data:
    cmd = line.split()[0]
    try:
      V = int(line.split()[1])
    except IndexError:
      V = None
    if cmd == "addx":
      assert V
      for _ in range(2):
        cycles += 1
        if cycles in [20, 60, 100,140, 180, 220]:
          signal_strength = cycles * X
          result += signal_strength
          print(f"{cmd=}, {V=}, {X=}, {cycles=}, {signal_strength=}")
      X += V
    elif cmd == "noop":
      for _ in range(1):
        cycles += 1
        if cycles in [20, 60, 100,140, 180, 220]:
          signal_strength = cycles * X
          result += signal_strength
          print(f"{cmd=}, {V=}, {X=}, {cycles=}, {signal_strength=}")
    else:
      continue
  return result


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  def print_CRT():
    for crt in CRTS:
      print(crt)

  def print_sprite():
    sprite = ""
    for i in range(40):
      if i == (X + 1) or i == (X - 1) or i == X:
        sprite += "#"
      else:
        sprite += "."
    print("sprite: ", sprite)

  CRTS = []
  CRT = ""

  X = 1
  sprite_pos = X

  cycles = 0
  for line in data:
    cmd = line.split()[0]
    try:
      V = int(line.split()[1])
    except IndexError:
      V = None
    if cmd == "addx":
      assert V
      for _ in range(2):
        if sprite_pos == len(CRT) or sprite_pos-1 == len(CRT) or sprite_pos+1 == len(CRT):
          CRT += "#"
        else:
          CRT += "."
        cycles += 1
        if len(CRT) == 40:
          CRTS.append(CRT)
          CRT = ""
      X += V
      sprite_pos = X
    elif cmd == "noop":
      for _ in range(1):
        if sprite_pos == len(CRT) or sprite_pos-1 == len(CRT) or sprite_pos+1 == len(CRT):
          CRT += "#"
        else:
          CRT += "."
        cycles += 1
        if len(CRT) == 40:
          CRTS.append(CRT)
          CRT = ""
  print_CRT()
  return None
