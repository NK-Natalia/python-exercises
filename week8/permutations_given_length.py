from itertools import permutations
print(
    *map(
        lambda x: ''.join(map(str, x)),
            permutations(
                map(
                    lambda x: x,
                    range(1, int(input()) + 1)
                    )
                )
        ), sep='\n'
    )
