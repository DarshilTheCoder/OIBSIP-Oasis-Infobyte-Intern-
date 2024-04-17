import string
import random as rd

letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation

class GeneratePassword:
    
    def __init__(self,password_length):
        self.password_length = password_length
        self.password= ""
        
    def simple_password(self):
        for i in range(0,self.password_length):
            self.password+=rd.choice(letters)
        self.password_list = list(self.password)
        rd.shuffle(self.password_list)
        self.password = "".join(self.password_list)
        return self.password
    
    def medium_password(self):
        for i in range(0,self.password_length):
            self.password+=rd.choice(letters)
            if len(self.password)==self.password_length:
                break
            self.password+=rd.choice(numbers)
            if len(self.password)==self.password_length:
                break
        print('length of password is = ',len(self.password))
        self.password_list = list(self.password)
        rd.shuffle(self.password_list)
        self.password = "".join(self.password_list)
        return self.password

    def strong_password(self):
        for i in range(0,self.password_length):
            self.password+=rd.choice(letters)
            if len(self.password)==self.password_length:
                break
            self.password+=rd.choice(numbers)
            if len(self.password)==self.password_length:
                break
            self.password+=rd.choice(punctuations)
            if len(self.password)==self.password_length:
                break
        print('length of strong password is = ',len(self.password))
        self.password_list = list(self.password)
        rd.shuffle(self.password_list)
        self.password = "".join(self.password_list)
        return self.password