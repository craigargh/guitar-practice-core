def level_one_picked_metal_patterns(length=None):
    patterns = [
        [2, 3, 2, 1],
        [1, 3, 2, 1],
        [6, 4, 3, 1],
        [3, 4, 5, 4, 3, 2, 2, 1],
        [5, 8, 7, 5, 6, 5, 1, 2],
        [6, 5, 4, 3, 2, 3, 2, 1],

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
