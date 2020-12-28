import re

def abbreviate(words):

    #extract all the words
    list_of_words = re.findall(r"[a-z]+'?[a-z]+|[a-z]+|\d+", words.lower())

    acronym_list = ""
    
    #add each first letter
    for x in list_of_words:
        acronym_list += x[0]

    #return string in upper case
    return acronym_list.upper()
    
