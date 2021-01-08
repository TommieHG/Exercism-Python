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

        #convert string items to integer items
        int_list = list(map(int, num_list))

        #the luhn algorithm
        for i in range(1, len(int_list), 2):
            int_list[i] *= 2
            
            if int_list[i] > 9:
                int_list[i] -= 9
        
        return sum(int_list) % 10 == 0
