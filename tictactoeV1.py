import itertools

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied, choose another!")
            return game_map, False
        if not just_display:
            game_map[row][column] = player
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError:
        print("Did you try to play a row or column outside of 0, 1, or 2? (IndexError)")
        return game_map, False
    except Exception as e:
        print(str(e))
        return game_map, False

def win(current_game):
    #check 3 in a row

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    for row in game:
        if all_same(row):
            print("Winner!")
            print(f"PLayer {row[0]} is the winner horizontally!")
            return True

    #check 3 in a column
    for col in range(len(current_game[0])):
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    #check 3 in a diagonal
    diags = []
    reversediags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
        reversediags.append(current_game[len(current_game)-ix-1][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally!")
        return True
    if all_same(reversediags):
        print(f"Player {diags[0]} has won diagonally!")
        return True

    return False

    

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_cycle = itertools.cycle(players)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player: {current_player}")
            column_choice = int(input("Which column?"))
            row_choice = int(input("Which row?"))

            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Byeeee")
                play = False
            else:
                print("Not a valid answer, so... c u l8r alligator")
                play = False

