"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized, and remaining letters lowercased.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Example

' Hello there thanks for trying my Kata'  =>  "#HelloThereThanksForTryingMyKata"
'    Hello     World   '                  =>  "#HelloWorld"
''                                        =>  false

"""

def generate_hashtag(s: str):
    word_list = []
    list_string = ""

    for chars in s:
        if chars != " ":
            list_string += chars
        elif 
        else:
            print("space detected")

    
        print(list_string)
        word_list.append(list_string)





# figure out a way to sanitise the strings into single space strings
# capitalise first letter in each word
# add hashtag to first index of string

generate_hashtag("   codewars    is nice")