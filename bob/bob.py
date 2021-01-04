import re

def response(hey_bob):

    #carve out everything that is not whitespace
    q = re.findall(r"\S", hey_bob)
    
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif len(re.findall(r"\s", hey_bob)) == len(hey_bob):
        return "Fine. Be that way!"
    elif q[-1] is "?":
        return "Sure."
    else:
        return "Whatever."
