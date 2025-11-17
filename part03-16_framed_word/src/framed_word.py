word = input("Word: ")

width = 30
block = "*" * width

# The spacer length is calculated by taking the width of the frame, minus the
# two blocks at the start/end, minus the length of the word, and we divide it
# by 2, while rounding the result down to a even number
spacer_length = (width - 2 - len(word)) // 2

start_spacer = " " * spacer_length

# If the length of the word is an odd number, we add an extra space (1) to the
# end spacer, to make sure the row width will be 30 characters.
extra_spaces = len(word) % 2
end_spacer = " " * (spacer_length + extra_spaces)

print(block)
print("*" + start_spacer + word + end_spacer + "*")
print(block)
