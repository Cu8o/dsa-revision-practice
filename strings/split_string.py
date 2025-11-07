"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters,
then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


def solution(s: str) -> list:

    chars_list = []
    counter = 0
    
    for chars in range(len(s)):
        counter += 1
        
        if counter % 2 == 0:
            chars_list.append(s[chars-1]+s[chars])
            
        elif counter / len(s) == 1:
            chars_list.append(s[chars]+"_")

            
    return chars_list

"""
This works by iterating through the indexes of the string, every iteration we add +1 to our counter
Because we're looking for every 2 character intervals, when counter is even, we add that char at the current index and is previous char to the list
This will map all the char pairs in an even totalled string
Once this is exhausted, logic runs to get counter total / string length = 1 (which it will always do)
This captures the last index and add '_' to the character then adds it to the list 
"""
