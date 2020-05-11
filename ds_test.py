import math

import numpy as np
from itertools import combinations_with_replacement


# 1
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


# 2
"""
Some assumptions I made so I could solve this exercise:
1. All elements are integers. This is not explicit said and I based this
only on the options given
2. The set can be of any possible size. Different sets can lead to the same
mean and the size is also not given, so I'm using what is convenient (:
3. At least 4 of the possible options should be in the set.
Ok, given this, my answer is option A) 30.
First of all, the only rule explicit in the question is that
  x_max = 5 + 2*x_min
so, if x_min = 30, x_max = 90 and all other options greater than x_max
would be outside the set
from 50 on, it's possible to find a set with all the options and mean = 100
for example [50,70,71,70,120,154,155], where x_min = 50 and x_max = 155,
statisfying the x_max = 5 + 3*x_min condition
"""


# 3
def get_stats(sample):

    sample_mean = mean(sample)
    sample_std = std(sample)
    sample_mode = mode(sample)
    sample_mode = median(sample)
    sample_median = median(sample)

    sample_sem = sem(sample)

    stats = {"mean": sample_mean,
             "std": sample_std,
             "sem": sample_sem,
             "mode": sample_mode,
             "median": sample_median}

    return stats


def mean(sample):

    sample_size = len(sample)
    result = 0

    for i in sample:
        result += i

    return result/sample_size


def median(sample):

    sorted_sample = sorted(sample)
    sample_size = len(sample)

    if sample_size % 2 == 0:
        # since our arrays start at 0, we have to use i-1 and 1 to get the
        # median value
        sample_median = sorted_sample[sample_size//2-1] + \
                        sorted_sample[sample_size//2]
    else:
        sample_median = sorted_sample[sample_size // 2]

    return sample_median


def std(sample):

    sample_size = len(sample)
    sample_mean = mean(sample)

    result = 0
    for i in sample:
        result += (i - sample_mean)**2

    return result/sample_size


def mode(sample):

    return np.bincount(sample).argmax()


def sem(sample):

    sample_size = len(sample)
    return std(sample)/math.sqrt(sample_size)


# 4
"""
Considering that the costumers buy ONLY in the store of the mentioned
probability (this is not explicit in the question), we have
50% buying in A, 30% buying in B and 20% buying in C

a.
for A, the answer rate is 50%. so 50% of the costumers did not answer.
so here we have 50% (not-answering-rate) of 50% (costumer that buy at A)
and we can manage to find our P(didn't answer|A) = 0.5*0.5 = 0.25
using the same technique, we have P(didn't answer|B) = 0.4*0.3 = 0.12 and
P(didn't answer|C) = 0.1*0.2 = 0.02

now, knowing the "didn't aswer rate" of all three stores, we can know too
the general rate by summing them: 0.25 + 0.12 + 0.02 = 0.39 or 39%. so this
is the probability that a random customer didn't answer the campaign.

b.
to find out a responder that went to C, we can apply Bayes
P(C|answered) = P(answered|C) * P(C)/P(answered)
             = 0.9 * 0.2 / 0.61
             = 0.2951
So the probability is 29.51%
"""


# 5
"""
The probability of getting one the b type dice (P(b))is 3/12 and the
probability of getting a six is 0.85, so the conditional probability is of
0.2125 or 21.25%
"""
