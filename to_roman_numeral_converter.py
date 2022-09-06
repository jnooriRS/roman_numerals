class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for numeral in range(len(s)):
            if numeral + 1 < len(s) and roman_table[numeral] < roman_table[numeral + 1]:
                result -= roman_table[numeral]
            else:
                result += roman_table[numeral]

        return result


Solution("MCMXCIV")