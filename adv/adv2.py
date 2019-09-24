def intersection(*lists):
    if not lists:
        return set()

    if len(lists) == 1:
        return set()

    sets = [set(curr) for curr in lists]
    initial_set = sets.pop()

    intersection_set = set()

    for value in initial_set:
        intersections = 0
        for other_set in sets:
            if value in other_set:
                intersections += 1

        if intersections == len(sets):
            intersection_set.add(value)

    return intersection_set


from functools import reduce


def main():
    print(intersection([4, 5, 6, 8], [4, 5, 9, 8], [5, 6, 8]))

    reduce(lambda x, y: set(x) & set(y), [[4, 5, 6, 8], [4, 5, 9, 8], [5, 6, 8]])
    # or
    reduce(lambda x, y: x & y, [set([4, 5, 6, 8]), set([4, 5, 9, 8]), set([5, 6, 8])])

    def count(histogram, word):

        if histogram[word]:
            histogram[word] += 1
        else:
            histogram[word] = 1

        return histogram

    print(
        reduce(
            lambda x, y: dict(
                list(x.items())
                + list(y.items())
                + [(k, x[k] + y[k]) for k in set(x) & set(y)]
            ),
            list(
                map(
                    lambda x: {x: 1},
                    [
                        "Deer",
                        "Bear",
                        "River",
                        "Car",
                        "Car",
                        "River",
                        "Deer",
                        "Car",
                        "Bear",
                    ],
                )
            ),
        )
    ),


if __name__ == "__main__":
    main()
