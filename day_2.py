# Advent of Code - Day 2

def determineMoveScore(opponent_move, self_move):
    MOVE_POINTS = {
        'X': 1,  # Rock
        'Y': 2,  # Paper
        'Z': 3  # Scissors
    }
    WIN_POINTS = 6
    DRAW_POINTS = 3

    # I have both 'XYZ' and 'RPS' to account for part 1 & 2 since I'm lazy :)
    if opponent_move == 'A':  # Rock
        if self_move == 'X' or self_move == 'R':
            return MOVE_POINTS['X'] + DRAW_POINTS
        if self_move == 'Y' or self_move == 'P':
            return MOVE_POINTS['Y'] + WIN_POINTS
        if self_move == 'Z' or self_move == 'S':
            return MOVE_POINTS['Z']
    if opponent_move == 'B':  # Paper
        if self_move == 'X' or self_move == 'R':
            return MOVE_POINTS['X']
        if self_move == 'Y' or self_move == 'P':
            return MOVE_POINTS['Y'] + DRAW_POINTS
        if self_move == 'Z' or self_move == 'S':
            return MOVE_POINTS['Z'] + WIN_POINTS
    if opponent_move == 'C':  # Scissors
        if self_move == 'X' or self_move == 'R':
            return MOVE_POINTS['X'] + WIN_POINTS
        if self_move == 'Y' or self_move == 'P':
            return MOVE_POINTS['Y']
        if self_move == 'Z' or self_move == 'S':
            return MOVE_POINTS['Z'] + DRAW_POINTS


def computeOldScore():
    total_score = 0

    with open("inputs/day-2.txt", 'r') as f:
        games = f.readlines()

    for game in games:
        moves = game.strip().split(' ')
        opponent_move, self_move = moves

        total_score += determineMoveScore(opponent_move, self_move)

    return total_score


def determineMove(opponent_move, self_strategy):
    LOSE = {
        'A': 'S',
        'B': 'R',
        'C': 'P'
    }

    DRAW = {
        'B': 'P',
        'A': 'R',
        'C': 'S'
    }

    WIN = {
        'A': 'P',
        'B': 'S',
        'C': 'R'
    }

    if self_strategy == 'X':
        return LOSE[opponent_move]
    if self_strategy == 'Y':
        return DRAW[opponent_move]
    if self_strategy == 'Z':
        return WIN[opponent_move]


def computeNewScore():
    total_score = 0

    with open("inputs/day-2.txt", 'r') as f:
        games = f.readlines()

    for game in games:
        moves = game.strip().split(' ')
        opponent_move, self_strategy = moves
        self_move = determineMove(opponent_move, self_strategy)

        total_score += determineMoveScore(opponent_move, self_move)

    return total_score


if __name__ == "__main__":
    answer_a = computeOldScore()
    answer_b = computeNewScore()

    print("Part A: ", answer_a)
    print("Part B: ", answer_b)
