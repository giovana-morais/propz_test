from itertools import combinations_with_replacement

def game(print_round=False):

    hunter_winnings = 0
    moose_winnings = 0

    total, dice_probs = get_possibilities()

    idx = 0
    for new_game in dice_probs:
        idx += 1
        hunter_position = 1
        moose_position = 5
        moose_house = 12
        for dice_value in new_game:
            hunter_position, moose_position = move(hunter_position,
                                                   moose_position,
                                                   dice_value)
            if hunter_position >= moose_position:
                hunter_winnings += 1
                if print_round:
                    print_round_stats(new_game,
                                      hunter_position,
                                      moose_position)
                break
            elif moose_position >= moose_house:
                moose_winnings += 1
                if print_round:
                    print_round_stats(new_game,
                                      hunter_position,
                                      moose_position)
                break
    print_game_stats(total, hunter_winnings, moose_winnings)
    return hunter_winnings / total, moose_winnings / total


def print_game_stats(total, hunter_winnings, moose_winnings):

    print(f"total possible game: {total}")
    print(f"total hunter winnings: {hunter_winnings}" +
          f"({hunter_winnings*100/total:.2f}%)")
    print(f"total moose winnings: {moose_winnings}" +
          f"({moose_winnings*100/total:.2f}%)")


def print_round_stats(new_game, hunter_position, moose_position):

    print(f"dices: {new_game}")
    if hunter_position >= moose_position:
        print("hunter wins")
    else:
        print("moose wins")
    print(f"hunter position: {hunter_position}" +
          f"moose position {moose_position}")
    print("="*80)


def get_possibilities():

    possibilities = list(combinations_with_replacement([1, 2, 3, 4, 5, 6], 6))

    return len(possibilities), possibilities


def move(hunter, moose, dice):

    moose_movements = [1, 2, 3, 4]
    if dice in moose_movements:
        new_moose_position = moose + dice
        new_hunter_position = hunter
    else:
        new_moose_position = moose
        new_hunter_position = hunter + dice

    return new_hunter_position, new_moose_position
