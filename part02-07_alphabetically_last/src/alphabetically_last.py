word_a = input("Please type in the 1st word: ")
word_b = input("Please type in the 2nd word: ")

if word_b > word_a:
    print(f"{word_b} comes alphabetically last.")
elif word_a > word_b:
    print(f"{word_a} comes alphabetically last.")
else:
    print("You gave the same word twice.")
