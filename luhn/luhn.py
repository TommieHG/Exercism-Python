import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):

        #filter non-digits
        if((len(re.findall(r"\D", self.card_num)) - len(re.findall(r"\s", self.card_num))) > 0):
            return False

        #extract each digit and reverse to make algorithm easier to perform
        num_list = re.findall(r"[0-9]", self.card_num)
        num_list.reverse()

        #filter short strings
        if(len(num_list) < 2):
           return False
           
        #turn string data type to int data type
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])

        #the luhn algorithm
        for i in range(1, len(num_list), 2):
            num_list[i] *= 2
            
            if num_list[i] > 9:
                num_list[i] -= 9
        
        return sum(num_list) % 10 == 0
