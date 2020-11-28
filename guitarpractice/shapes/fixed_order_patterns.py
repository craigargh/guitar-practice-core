from itertools import product


def picked_metal_patterns(length=None):
    patterns = [
        *four_contiguous_position_patterns(),

        [6, 4, 3, 1],

        [3, 4, 5, 4, 3, 2, 2, 1],
        [5, 8, 7, 5, 6, 5, 1, 2],
        [6, 5, 4, 3, 2, 3, 2, 1],
        [1, 2, 3, 6, 8, 7, 5, 4],

        [2, 1, 2, 3, 2],

        [4, 3, 1, 2, 5, 6],

        [2, 2, 3, 2, 1, 4, 3, 3, 4],
        [2, 5, 4, 4, 3, 3, 2, 2, 1, 1],
    ]

    if length:
        patterns = [
            pattern
            for pattern in patterns
            if len(pattern) == length
        ]

    return patterns


def four_contiguous_position_patterns():
    """
     All variations of four contiguous note pick patterns where each note can only repeat twice at most
     with no two notes repeating twice each
    """
    return [
        sequence
        for sequence in product(range(1, 5), repeat=4)
        if len(set(sequence)) == 3 or len(set(sequence)) == 4
    ]
