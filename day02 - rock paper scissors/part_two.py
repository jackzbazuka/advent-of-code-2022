opponent_score_map = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def main() -> int:
    """
    Returns:
        total_strategy_score: int
    """
    score = 0

    with open("strategies.in", "r") as f:

        for strategy in f:
            opponent, outcome = strategy.strip().split(" ")

            if outcome == "X":
                if opponent == "A":
                    score += 3
                elif opponent == "B":
                    score += 1
                else:
                    score += 2
            elif outcome == "Y":
                score += opponent_score_map[opponent] + 3
            elif outcome == "Z":
                score += 6
                if opponent == "A":
                    score += 2
                elif opponent == "B":
                    score += 3
                else:
                    score += 1

    return score


if __name__ == "__main__":
    strategy_score = main()
    print(strategy_score)
