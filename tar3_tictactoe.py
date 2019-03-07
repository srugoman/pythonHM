def checkrows(game):
    for x in game:
        prev = x[0]
        won = True
        for player in x:
            if player != prev or won == False:
                won = False
                break
            prev = player
        if won == True:
            return True
    return False





def main():
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    print(checkrows(game))



if __name__ == "__main__":
    main()
