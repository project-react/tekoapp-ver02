import re 
from tekoapp.extensions import exceptions

class Username:
    value = ''
    def __init__(self, value):
        self.value = value

    def test_length(self):
        return len(self.value) >= 6

    def test_has_space(self):
        result = re.search(r'[^\S+$]+', self.value)
        if result:
            return False
        else:
            return True

    def test_charater(self):
        result = re.search(r'[a-zA-Z0-9]+$', self.value)
        if result:
            return True
        else:
            return False

    def is_valid(self):
        return self.test_length() and self.test_has_space() and self.test_charater()

class Email:
    value = ''
    def __init__(self, value):
        self.value = value
    
    def test_format(self):
        result = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', self.value, re.I)
        if result:
            return True
        else:
            return False

    def is_valid(self):
        return self.test_format()

class Password:
    value = ''
    def __init__(self, value):
        self.value = value

    def test_length(self):
        return len(self.value) >= 8

    def test_format(self):
        result = re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])', self.value)
        if result:
            return True
        else:
            return False

    def is_valid(self):
        return self.test_length() and self.test_format()

class NewPassword(Password):
    pass



def validator_before_handling(func):
    def inner(*args, **kwargs):
        for k, v in kwargs.items():
            if (k == "username" and Username(v).is_valid() == False):
                raise exceptions.BadRequestException("Data invalid!")
            elif (k == "email" and Email(v).is_valid() == False):
                raise exceptions.BadRequestException("Data invalid!")
            elif (k == "password" and Password(v).is_valid() == False):
                raise exceptions.BadRequestException("Data invalid!")
            elif (k == "newpassword" and NewPassword(v).is_valid() == False):
                raise exceptions.BadRequestException("Data invalid!")
        return func(*args, **kwargs)
    return inner
