from string import ascii_uppercase

lines: list[list[str]] = [[ascii_uppercase[0]]]

layers = int(input("Layers: "))

for i in range(1, layers):
    current_letter = ascii_uppercase[i]

    for line in lines:
        # Add the current letter to the left and right of the line.
        line.insert(0, current_letter)
        line.append(current_letter)

    # Add a top and a bottom line, filled with the current letter.
    current_width = len(lines[0])
    top_bottom_line = [current_letter for j in range(current_width)]

    lines.insert(0, top_bottom_line)
    lines.append(top_bottom_line[:])

for line in lines:
    print("".join(line))
