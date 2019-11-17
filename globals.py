game = "I want to play a game"
print(id(game))

def game_board():
    global game
    print(id(game))
    game = "A game"
    print(id(game))
    return game

game_board()
print(game)
