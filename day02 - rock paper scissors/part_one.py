opponent_score_map = {
    "A": 1,
    "B": 2,
    "C": 3,
}

player_score_map = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def main() -> int:
    """
    Returns:
        total_strategy_score: int
    """
    score = 0

    with open("strategies.in", "r") as f:

        for strategy in f:
            opponent, player = strategy.strip().split(" ")
            score += player_score_map[player]

            if opponent_score_map[opponent] == player_score_map[player]:
                score += 3
            else:
                if abs(opponent_score_map[opponent] - player_score_map[player]) == 2:
                    if opponent_score_map[opponent] > player_score_map[player]:
                        score += 6
                elif (opponent_score_map[opponent] + player_score_map[player]) >= 3:
                    if opponent_score_map[opponent] < player_score_map[player]:
                        score += 6

    return score


if __name__ == "__main__":
    strategy_score = main()
    print(strategy_score)
