import math
import numpy as np


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

    print(stats)
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

    return math.sqrt(result/sample_size)


def mode(sample):

    return np.bincount(sample).argmax()


def sem(sample):

    sample_size = len(sample)
    return std(sample)/math.sqrt(sample_size)
