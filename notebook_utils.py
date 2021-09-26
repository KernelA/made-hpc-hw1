import numpy as np


def log_transform(data):
    return np.log10(data)


def inverse_log_transform(data):
    return 10 ** data
