from __future__ import annotations

UNMASKED_NUMBERS = 4


def censor(card_number: str) -> str | None:
    if not is_valid(card_number=card_number):
        return None

    censored_card_number = ""
    unmasked_characters_count = 0

    for char in reversed(card_number):
        if char == " ":
            censored_card_number += char
            continue

        if unmasked_characters_count < UNMASKED_NUMBERS:
            censored_card_number += char
            unmasked_characters_count += 1
            continue

        censored_card_number += "x"

    return "".join(reversed(censored_card_number))


def is_valid(card_number: str) -> bool:
    sanitized_card_number = card_number.replace(" ", "")

    if not sanitized_card_number:
        return False
    if len(sanitized_card_number) < 13:
        return False
    if len(sanitized_card_number) > 19:
        return False
    if any(c.isalpha() for c in sanitized_card_number):
        return False

    return True
