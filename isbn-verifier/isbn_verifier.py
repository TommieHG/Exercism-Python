import re

def is_valid(isbn):
    list_of_numbers = re.findall(r"\w", isbn)
    
    #remove too short or long numbers
    if len(list_of_numbers) is not 10:
        return False

    #remove chars in the middle of sequence
    for i in range(0,9):
        if not list_of_numbers[i].isdigit():
            return False

    #change X to 10 or return false if it is anything else
    if "X" in list_of_numbers[9]:
        list_of_numbers[list_of_numbers.index("X")] = '10'
    elif list_of_numbers[9].isalpha():
        return False

    #add and multiply according to algorithm
    sum = 0
    for i in range(len(list_of_numbers)):
        sum += int(list_of_numbers[i]) * (10 - i)

    return sum % 11 == 0
        
