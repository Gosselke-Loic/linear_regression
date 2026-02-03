from numpy import ndarray


def normalize(array: ndarray) -> list[float]:
    " Normalize an array "

    min_m = min(array)
    max_m = max(array)

    normalized_array: list[float] = [(x - min_m) /
                                     (max_m - min_m) for x in array]

    return normalized_array


def normalize_one(array: ndarray, value: int) -> float:
    """ Normalize one value from an given array """

    min_m = min(array)
    max_m = max(array)

    normalized_value = (value - min_m) / (max_m - min_m)

    return normalized_value
