import sqlite3
from client import Client
import sql_manage_queries

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    cursor.execute(sql_manage_queries.CREATE_TABLE)


def change_message(new_message, logged_user):
    cursor.execute(sql_manage_queries.CHANGE_CLIENT_MESSAGE, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)
    
def change_pass_for_email(new_pass, username, email):    
    cursor.execute(sql_manage_queries.CHANGE_CLIENT_PASS_FROM_USERNAME_AND_EMAIL, (new_pass, username, email))
    conn.commit()

def change_pass(new_pass, logged_user):
    cursor.execute(sql_manage_queries.CHANGE_CLIENT_PASS, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    cursor.execute(sql_manage_queries.REGISTER_USER, (username, password))
    conn.commit()


def login(username, password):
    cursor.execute(sql_manage_queries.SELECT_USER, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False

def show_email(username):
    cursor.execute(sql_manage_queries.SELECT_USER_EMAIL)
    return cursor.fetchone()

