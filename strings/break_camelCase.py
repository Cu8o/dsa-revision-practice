"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example:
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s: str) -> str:
    string = ""
    for char in s:
        if char == char.upper():
            string = string + " " + char
        else:
            string += char
    return string

"""
1. Scan along the string
2. Find a capital letter
3. When I've found the capital letter, insert a space in the previous index

"""

