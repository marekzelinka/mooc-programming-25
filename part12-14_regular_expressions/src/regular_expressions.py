# Write your solution here
import re


def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|S(at|un)", my_string) is not None


if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))
    print()


def all_vowels(my_string: str):
    return re.search("^[aeiou]+$", my_string) is not None


if __name__ == "__main__":
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))
    print()


def time_of_day(my_string: str):
    return re.search(r"^(1\d|2[0-3]):[0-5]\d:[0-5]\d$", my_string) is not None


if __name__ == "__main__":
    print(time_of_day("19:zz:04"))
    print(time_of_day("20:10:30"))
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
