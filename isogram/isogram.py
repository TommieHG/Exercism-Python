def is_isogram(string):
    #filter all that is not letters in a lower case version
    newstring = list(filter(str.isalpha, string.lower()))

    #set() returns a unique set of unordered elements
    return len(newstring) == len(set(newstring))
