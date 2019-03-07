def checkrows(game):
    for row in game:
        prev = row[0]
        won = True
        for player in row:
            if player != prev:
                won = False
                break
        if won == True:
            return player
    return 0


def checkcols(game):
    first = game [0]
    i = 0
    for player in first:
        prev = player
        won = True
        for row in game:
            if row[i] != prev:
                won = False
                break
        if won == True:
            return prev
        i += 1
    return 0


def main():
    game = [[1, 0, 1],
            [2, 1, 0],
            [2, 1, 1]]
    print(checkcols(game))


if __name__ == "__main__":
    main()
