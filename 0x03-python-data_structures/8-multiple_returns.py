#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        return (0, None)
    else:
        # Return the length of the string and its first character
        return (len(sentence), sentence[0])
