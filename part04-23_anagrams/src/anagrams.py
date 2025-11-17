def anagrams(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    print(anagrams("tame", "meta"))
