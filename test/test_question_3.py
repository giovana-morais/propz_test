import numpy as np
import question.question_3 as stats
import pytest


def test_mean():
    sample = np.arange(1,10)

    assert stats.mean(sample) == 5

def test_std():
    sample = np.arange(1,10)

    assert stats.std(sample) == 2.581988897471611

def test_mode():
    sample = np.array([1,2,3,3,4,5,5,5])

    assert stats.mode(sample) == 5

def test_sem():
    sample = np.arange(1,10)

    assert stats.sem(sample) == 0.8606629658238704

def median():
    sample = np.arange(1,10)

    assert stats.median(sample) == 5
