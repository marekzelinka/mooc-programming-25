def read_matrix() -> list[list[int]]:
    matrix: list[list[int]] = []

    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            raw_numbers = line.split(",")

            row: list[int] = []

            for raw_number in raw_numbers:
                number = int(raw_number)

                row.append(number)

            matrix.append(row)

    return matrix


def combine(list: list) -> list:
    result = []

    for item in list:
        result += item

    return result


def matrix_sum() -> int:
    matrix = read_matrix()
    combined_rows = combine(matrix)

    return sum(combined_rows)


def matrix_max() -> int:
    matrix = read_matrix()
    combined_rows = combine(matrix)

    return max(combined_rows)


def row_sums() -> list[int]:
    matrix = read_matrix()

    sums = []

    for row in matrix:
        row_sum = sum(row)

        sums.append(row_sum)

    return sums


def main() -> None:
    sum_of_matrix = matrix_sum()
    print(sum_of_matrix)

    max_of_matrix = matrix_max()
    print(max_of_matrix)

    sum_of_rows = row_sums()
    print(sum_of_rows)


if __name__ == "__main__":
    main()
