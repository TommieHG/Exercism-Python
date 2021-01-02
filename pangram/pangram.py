def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lowsent = sentence.lower()
    
    for k in range(len(alphabet)):
        x = lowsent.find(alphabet[k])
        if x is -1:
            return False

    return True
