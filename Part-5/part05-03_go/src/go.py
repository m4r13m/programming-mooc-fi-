def who_won(game_board: list):
    score1 = 0
    score2 = 0
    for row in game_board:
        for square in row:
            if square == 1:
                score1 += 1
            elif square == 2:
                score2 += 1
    if score1 > score2:
        return 1
    elif score1 < score2:
        return 2
    else:
        return 0

if __name__=="__main__":
    gb = [[0,1,1], [0,1,1],[2,2,2]]
    print(who_won(gb))