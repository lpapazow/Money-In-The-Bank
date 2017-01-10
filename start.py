import sql_manager
import sql_manage_queries
import getpass
from client import Client
import hashlib
import smtplib
import os
import time


class MainMenu():
    def __init__(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")
        self.logged_user = None

        while True:
            command = input("$$$>")

            if command == 'register':
                username = input("Enter your username: ")
                password = Client.set_password(username)
                hashed = Client.hash_pass(password)

                sql_manager.register(username, hashed)

                print("Registration Successfull")

            elif command == 'login':
                username = input("Enter your username: ")
                password = getpass.getpass()
                hashed = Client.hash_pass(password)

                self.logged_user = sql_manager.login(username, hashed)

                if self.logged_user:
                    LoggedMenu(self.logged_user)
                else:
                    print("Login failed")

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
                
            elif "send-reset-password" in command:
                user_email = sql_manager.show_email()
                self.send_mail(user_email)
            
            elif "reset-password" in command:
                pass    
            
            else:
                print("Not a valid command")
        
    def send_mail(self, user_email):
        server = smtplib.SMTP('smtp.gmail.com', '587', 'localhost')
        fromaddr = 'lpapazow@gmail.com'
        toaddrs = user_email
        msg = hash_pass()
        username = 'lpapazow@gmail.com'
        password = os.environ['MY_SMTP_PASS']
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        sql_manager.change_pass(str(time.time), self.logged_user)
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()


class LoggedMenu():
    def __init__(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                sql_manager.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    MainMenu()

if __name__ == '__main__':
    main()
