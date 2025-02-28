# lib/main.py

from models.books import Books
from models.users import Users
from models.borrowed import Borrowed
from config import Database

#Database.drop_tables()
Database.create_tables()



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        else:
            print("Invalid choice")

def book_operations():
    while True:
        print("\n***Book Management***")
        print("\nPlease select an option:")
        print("1. Show all books")
        print("2. Add a new book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. display borrowed books")
        print("6. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            print(Books.show_all_books())
        elif choice == "2":
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            Books.register_book(book_title, book_author)
            print(f"{book_title} has been registered successfully!")
        elif choice == "3":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            borrower = input("Enter username: ")
            Borrowed.borrow_book(title, author, borrower)
            # print(f"{title} by {author} has been borrowed by {borrower}")
        elif choice == "4":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            borrower = input("Enter username: ")
            Borrowed.return_book(title, author, borrower)
            #print(f"{title} by {author} has been returned by {borrower}")
        elif choice == "5":
            print("\n***Borrowed Books***")
            print(Borrowed.all_borrowed_books())
        elif choice == "6":
            return menu()
        else:
            print("Invalid choice")

def user_operations():
    while True:
        print("\n***User Management***")
        print("\nPlease select an option:")
        print("1. Log in")
        print("2. Sign up")
        print("3. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            username = input("Enter username: ")
            passcode = input("Enter passcode: ")
            print("\nThank you for logging in!")
            print(f"\n {Users.show_user_profile(username, passcode)}")
            print("\n1. Update your profile")
            print("2. View your books")
            print("3. Return to main menu")
            choice = input("> ")
            if choice == "1":
                first_name = input("update your first name: ")
                last_name = input("update your last name: ")
                username = input("update username: ")
                passcode = input("update 6 digit passcode: ")
                if len(passcode) != 6:
                    print("Passcode must be 6 digits.")
                    break
                else:
                    Users.update_user_profile(first_name, last_name, username, passcode)
                    print(f"Your profile has been updated successfully!")
            
            if choice == "2":
                print("\nBooks you are borrowing:")
                print(f"\n{Borrowed.user_books(username)}")
        elif choice == "2":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            username = input("Create username: ")
            passcode = input("Create 6 digit passcode: ")
            if len(passcode) != 6:
                print("Passcode must be 6 digits.")
                break
            else:
                Users.register_user(first_name, last_name, username, passcode)
                print(f"{first_name} {last_name} has been registered successfully!")
        elif choice == "3":
            return menu()
        else:
            print("Invalid choice")

def menu():
    print("\n***Welcome to the Library!***")
    print("\nPlease select an option:")
    print("1. Book Management")
    print("2. User Profile")
    print("00. Exit the program")

def exit_program():
    print("Goodbye!")
    exit()


if __name__ == "__main__":
    main()
