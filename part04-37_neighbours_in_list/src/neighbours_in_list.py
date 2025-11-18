def longest_series_of_neighbours(numbers: list[int]) -> int:
    # We initialize the list with 1, representing the first series of neighbours within the list.
    neighbours_counts: list[int] = [1]

    for i in range(1, len(numbers)):
        # At the start of the loop, "before" represents the first number that we initially skipped, if the series is consecutive we update the count, if not we add a new one.
        before = numbers[i - 1]
        current = numbers[i]

        diff = abs(before - current)

        if diff == 1:
            neighbours_counts[-1] += 1
        else:
            neighbours_counts.append(1)

    # We gathered the lengths of the series of neighbours and pick the biggest one.
    return max(neighbours_counts)


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]

    print(longest_series_of_neighbours(my_list))  # 4
