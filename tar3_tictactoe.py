def checkrows(game):
    global player
    for row in game:
        prev = row[0]
        won = True
        for player in row:
            if player != prev:
                won = False
                break
        if won:
            return player
    return 0


def checkcols(game):
    first = game[0]
    i = 0
    for player in first:
        prev = player
        won = True
        for row in game:
            if row[i] != prev:
                won = False
                break
        if won:
            return prev
        i += 1
    return 0


def checkobliques(game):
    rowlen = len(game[0]) - 1
    i = 1
    prev1 = game[0][0]
    prev2 = game[0][rowlen]
    ob1 = True
    ob2 = True
    while i <= rowlen:
        if game[i][i] != prev1:
            ob1 = False
        if game[i][rowlen-i] != prev2:
            ob2 = False
        if (not ob1) and (not ob2):
            return 0
        i += 1
    if ob1:
        return prev1
    if ob2:
        return prev2





def main():
    game = [[2, 0, 1],
            [2, 1, 0],
            [1, 1, 1]]
    print(checkobliques(game))


if __name__ == "__main__":
    main()
