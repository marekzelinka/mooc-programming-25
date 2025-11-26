from datetime import datetime
from string import digits


def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    date_of_birth = pic[:6]
    century_marker = pic[6]
    personal_id = pic[7:10]
    control_char = pic[-1]

    # Validate all the provided numbers, so that converting strings to numbers will not throw an error
    control_numbers = date_of_birth + personal_id
    for number in control_numbers:
        if number not in digits:
            return False

    century_markers = {"+": 1800, "-": 1900, "A": 2000}
    if century_marker not in century_markers.keys():
        return False
    century = century_markers[century_marker]

    day = int(date_of_birth[:2])
    month = int(date_of_birth[2:4])
    base_year = int(date_of_birth[4:])
    year = century + base_year

    try:
        datetime(year, month, day)
    except ValueError:
        return False

    valid_control_characters = digits + "ABCDEFHJKLMNPRSTUVWXYZ"
    character_index = int(control_numbers) % 31

    return valid_control_characters[character_index] == control_char
