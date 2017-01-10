import getpass
import validators
import hashlib

class Client():
    def __init__(self, id, username, password=None, balance=None, message=None, email=None):
        self.__username = username
        self.__balance = balance
        self.__passwrod = password
        self.__id = id
        self.__message = message
        self.__email = email

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message
        
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password

    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance < amount:
            print("You can't withdraw!")
            return False
        self.__balance -= amount
        return True
    
    def display_balance(self):
        print("Your current balance is {0}".format(self.__balance))

    @staticmethod
    def set_password(username):
        print("Select password")
        passw = getpass.getpass()
        while not validators.pass_is_valid(passw, username):
            print("Password too weak!")
            passw = getpass.getpass()
        return passw

    @staticmethod
    def hash_pass(password):
        return hashlib.sha1(password.encode('utf-8')).hexdigest()

