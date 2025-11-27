def find_words(search_term: str) -> list[str]:
    wordlist: list[str] = []

    with open("words.txt") as file:
        for line in file:
            word = line.strip()

            found = False

            if (search_term.startswith("*") and word.endswith(search_term[1:])) or (
                search_term.endswith("*") and word.startswith(search_term[:-1])
            ):
                found = True
            elif "." in search_term and len(word) == len(search_term):
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        break
                else:
                    found = True
            elif word == search_term:
                found = True

            if not found:
                continue

            wordlist.append(word)

    return wordlist


if __name__ == "__main__":
    print(find_words("ca."))
    # ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']
