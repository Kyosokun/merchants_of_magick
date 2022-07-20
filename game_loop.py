

def game_loop(game):
    while game.turn_number <= 10:
        game.playing_phase()
        game.orders_phase()
        game.mastery_phase()
        game.advance_turn()
