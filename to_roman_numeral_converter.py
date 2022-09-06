def to_arabic_number(s: str) -> int:
    roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for numeral in range(len(s)):
        if (
            numeral + 1 < len(s)
            and roman_table[s[numeral]] < roman_table[s[numeral + 1]]
        ):
            result -= roman_table[s[numeral]]
        else:
            result += roman_table[s[numeral]]

    return result


# Learnt from
# https://www.youtube.com/watch?v=3jdxYj3DD98
# https://www.youtube.com/watch?v=_5MYW7n1U-I


def to_roman_numeral(arabic_number: int) -> str:
    roman_table = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000],
    ]
    result = ""
    for roman_symbol, value in reversed(roman_table):
        if arabic_number // value:
            count = arabic_number // value
            result += roman_symbol * count
            arabic_number = arabic_number % value
    return result


# learnt from
# https://www.youtube.com/watch?v=ohBNdSJyLh8
