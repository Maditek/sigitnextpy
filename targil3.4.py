import string
import re


class UsernameContainsIllegalCharacterException(ValueError):
    def __init__(self, username, letter, index):
        self.username = username
        self.letter = letter
        self.message = "The username contains an illegal character " + f'"{letter}" at index {index}'
        super().__init__(self.message)


class UserNameTooShortException(ValueError):

    def __str__(self):
        return f"The username is too short"


class UserNameTooLongException(ValueError):
    def __str__(self):
        return f"The username is too long"


class PasswordMissingCharacterException(ValueError):
    def __str__(self):
        return f"The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacterException):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacterException):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacterException):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacterException):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShortException(ValueError):
    def __str__(self):
        return f"The password is too short"


class PasswordTooLongException(ValueError):
    def __str__(self):
        return f"The password is too long"


def check_input(username, password):
    allowed_letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_'
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_number = re.search(r'\d', password)
    has_special = re.search(f'[{re.escape(string.punctuation)}]', password)
    for letter in username:
        if letter not in allowed_letters:
            raise UsernameContainsIllegalCharacterException(username, letter, username.index(letter))
    if len(username) < 3:
        raise UserNameTooShortException
    if len(username) > 16:
        raise UserNameTooLongException
    if not has_upper:
       raise PasswordMissingUppercase
    if not has_lower:
       raise PasswordMissingLowercase
    if not has_number:
       raise PasswordMissingDigit
    if not has_special:
       raise PasswordMissingSpecial
    if len(password) < 8:
        raise PasswordTooShortException
    if len(password) > 40:
        raise PasswordTooLongException

    print("ok")




check_input("0123456789ABCDEFG", "2")
check_input("A_a1.", "12345678")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")