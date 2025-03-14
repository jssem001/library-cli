#users model lives here
from config import CONN, CURSOR

class Users:
    #register a new user
    @classmethod
    def register_user(cls, first_name, last_name, username, passcode):
        sql = "INSERT INTO users (first_name, last_name, username, passcode) VALUES (?,?,?,?)"
        CURSOR.execute(sql, (first_name, last_name, username, passcode))
        CONN.commit()
    
    #update user profile
    @classmethod
    def update_user_profile(cls, first_name, last_name, username, passcode):
        sql = "UPDATE users SET first_name = ?, last_name = ?, username = ?, passcode = ?"
        CURSOR.execute(sql, (first_name, last_name, username, passcode))
        CONN.commit()

    #display user profile
    @classmethod
    def show_user_profile(cls, username, passcode):
        sql = """
        SELECT first_name, last_name 
        FROM users
        WHERE username = ? AND passcode = ?
        """
        CURSOR.execute(sql,(username, passcode))
        profile = CURSOR.fetchone()

        if profile is None:
            return "Incorrect username or passcode. Please try again."
        else:
            return profile