def convert(number):
    res = ""
    
    if number % 3 is 0:
        res += "Pling"
    if number % 5 is 0:
        res += "Plang"
    if number % 7 is 0:
        res += "Plong"
    if res == "":
        res += str(number)

    return res
    
