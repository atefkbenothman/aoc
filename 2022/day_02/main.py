import logging
logger = logging.getLogger()


def part_1(data: list[str]) -> int:
  """
  part 1
  """
  hands = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
  }
  score_map = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
  }
  score = 0
  for line in data:
        opponent_hand, my_hand = hands[line.split()[0]], hands[line.split()[1]]
        if opponent_hand == "rock":
            if my_hand == "rock":
                score += 3
            elif my_hand == "paper":
                score += 6
            else:
                # scissors
                score += 0
        elif opponent_hand == "paper":
            if my_hand == "rock":
                score += 0
            elif my_hand == "paper":
                score += 3
            else:
                # scissors
                score += 6
        elif opponent_hand == "scissors":
            if my_hand == "rock":
                score += 6
            elif my_hand == "paper":
                score += 0
            else:
                # scissors
                score += 3
        else:
            print("ERROR")
            exit(0)
        score += score_map[my_hand]
  return score


def part_2(data: list[str]) -> int:
  """
  part 2
  """
  hands = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
  }
  needs_to_end = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
  }
  score_map = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
  }
  score = 0
  for line in data:
        opp_hand, outcome = hands[line.split()[0]], needs_to_end[line.split()[1]]
        if outcome == "draw":
            score += score_map[opp_hand]
            score += 3
        elif outcome == "lose":
            if opp_hand == "rock":
                score += score_map["scissors"]
            elif opp_hand == "paper":
                score += score_map["rock"]
            else:
                # scissors
                score += score_map["paper"]
            score += 0
        elif outcome == "win":
            if opp_hand == "rock":
                score += score_map["paper"]
            elif opp_hand == "paper":
                score += score_map["scissors"]
            else:
                # scissors
                score += score_map["rock"]
            score += 6
        else:
            print("ERROR")
            exit(0)
  return score
