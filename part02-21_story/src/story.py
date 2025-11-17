story = ""
prev_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == prev_word:
        print(story)
        break

    story += f"{word} "
    prev_word = word
