from typing import Union, Optional
import numpy as np


def log_transform(data):
    return np.log10(data)


def inverse_log_transform(data):
    return 10 ** data


def twatt2kwatt(value):
    return value * 1e9


def comma_number2str(number: str) -> Optional[Union[int, float]]:
    stripped_value = number.replace(",", "")
    try:
        value = int(stripped_value)
    except ValueError:
        try:
            value = float(stripped_value)
        except ValueError:
            return None

    return value
