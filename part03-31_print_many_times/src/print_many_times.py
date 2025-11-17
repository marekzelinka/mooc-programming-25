def print_many_times(text: str, times: int) -> None:
    while times > 0:
        print(text)

        times -= 1


if __name__ == "__main__":
    print_many_times("python", 5)
