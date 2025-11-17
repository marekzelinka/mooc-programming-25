word = input("Please type in a word: ")
query = input("Please type in a character: ")

start = word.find(query)
end = start + 3

if start != -1 and end < len(word):
    print(word[start:end])
