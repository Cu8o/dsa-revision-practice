"""
Parse nice int from char

You ask a small girl "How old are you?" She always says "x years old",
where x is a random number between 0 and 9.

Write a program that returns the girl's age as an integer.
Assume the first character in the string is always a number.
"""

def get_age(age: str) -> int:
    return int(age[0])
