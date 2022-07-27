UNITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

SCALES = ["hundred", "thousand", "million", "billion", "trillion"]

VALID_DASHES = [
    "twenty-",
    "thirty-",
    "forty-",
    "fifty-",
    "sixty-",
    "seventy-",
    "eighty-",
    "ninety-",
]


def word_to_number(string: str):
    string = string.lower()

    if not is_valid_word_number(string=string):
        return "Input not a string"

    mapping = build_word_map()

    current = 0
    result = 0
    for word in string.split():
        if "-" in word:
            for sub_word in word.split("-"):
                scale, increment = mapping[sub_word]
                current = current * scale + increment

                if scale > 100:
                    result += current
                    current = 0

        elif word not in mapping:
            return "Input not a string"

        else:
            scale, increment = mapping[word]
            current = current * scale + increment

            if scale > 100:
                result += current
                current = 0

    return result + current


def build_word_map():
    number_words = {"and": (1, 0)}
    for _id, word in enumerate(UNITS):
        number_words[word] = (1, _id)
    for _id, word in enumerate(TENS):
        number_words[word] = (1, _id * 10)
    for _id, word in enumerate(VALID_DASHES):
        number_words[word] = (1, _id * 10)
    for _id, word in enumerate(SCALES):
        number_words[word] = (10 ** (_id * 3 or 2), 0)

    return number_words


def is_valid_word_number(string: str) -> bool:
    dash_combination = build_valid_dashes_combination()
    for word in string.split():
        if "-" in word:
            if word not in dash_combination:
                return False
    return True


def build_valid_dashes_combination():
    combination = []
    ones = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for valid_dash in VALID_DASHES:
        for _word in ones:
            combination.append(f"{valid_dash}{_word}")
    return combination
