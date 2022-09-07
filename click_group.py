import click


@click.group()
def cli():
    pass


@cli.group()
# @click.argument("roman_numeral")
@click.option("--roman", prompt="Roman numeral to convert please", type=str)
def to_arabic_number(roman) -> int:
    roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for numeral in range(len(roman)):
        if (
            numeral + 1 < len(roman)
            and roman_table[roman[numeral]] < roman_table[roman[numeral + 1]]
        ):
            result -= roman_table[roman[numeral]]
        else:
            result += roman_table[roman[numeral]]

    print(result)
    # return result


@cli.group()
@click.option("--arabic_number", prompt="Integer you want to convert", type=int)
def to_roman_numeral(arabic_number) -> str:
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
    print(result)


if __name__ == "__main__":
    cli()
    to_roman_numeral()
    to_arabic_number()
