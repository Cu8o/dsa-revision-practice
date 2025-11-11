"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all words that have five or more letters reversed (just like the name of this kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Example
"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
"""

def spin_words(sentence: str):
    word_list = []
    word = ""

    for index in range(len(sentence)):
        word += sentence[index]
        if sentence[index] == " ":
            word_list.append(word[0:(len(word)-1)])
            word = ""
        elif index == len(sentence)-1:
            word_list.append(word[0:(len(word))])
    
    count = 0
    for word in word_list:
        if len(word) >= 5:
            word_list[count] = word[::-1]
        count += 1

    final_sentence = ""

    count = 0
    for words in word_list:
        count += 1
        if count == len(word_list):
            final_sentence += words
        else:
            final_sentence += words + " "

    return final_sentence

# iterate through string 
# capture and isolate words 
# if length of word is more than or equal to 5 
# reverse 
# return full sentence

