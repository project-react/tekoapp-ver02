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

    def test_characters(self):
        result = re.search(r'[a-zA-Z0-9]+$', self.value)
        if result:
            return True
        else:
            return False

    def test_special_characters(self):
        result = re.search(r'[!@#$%^&*(),.?":{}|<>-]', self.value)
        if result:
            return False
        else:
            return True

    def is_valid(self):
        return self.test_length() and self.test_has_space() and self.test_characters() \
               and self.test_special_characters()


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
            if (
                (k == "username" or k == "new_username")
                and
                False == (Username(v).is_valid())
            ):
                raise exceptions.BadRequestException("Data invalid!")
            elif (
                (k == "email" or k == "new_email")
                and
                False == (Email(v).is_valid())
            ):
                raise exceptions.BadRequestException("Data invalid!")
            elif (
                (k == "password" or k == "new_password")
                and
                False == (Password(v).is_valid())
            ):
                raise exceptions.BadRequestException("Data invalid!")
        return func(*args, **kwargs)
    return inner

