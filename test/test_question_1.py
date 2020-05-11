import pytest
import question.question_1 as game


def test_movements():
    hunter_position = 1
    moose_position = 1
    movement_size = 1

    new_hunter_position, new_moose_position = game.move(hunter_position,
                                                        moose_position,
                                                        movement_size)

    assert new_moose_position == moose_position + movement_size
    assert new_hunter_position == hunter_position

    movement_size = 6

    new_hunter_position, new_moose_position = game.move(hunter_position,
                                                        moose_position,
                                                        movement_size)

    assert new_moose_position == moose_position
    assert new_hunter_position == hunter_position + movement_size
