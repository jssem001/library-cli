# lib/main.py
from models.teams import Teams
from models.locations import Locations
from models.stadiums import Stadiums
from models.games import Games
from models.books import Books
from config import Database

Database.create_tables()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            team_operations()
        elif choice == "2":
            location_operations()
        elif choice == "3":
            stadium_operations()
        elif choice == "4":
            game_operations()
        elif choice == "5":
            book_operations()
        else:
            print("Invalid choice")

def book_operations():
    while True:
        print("\n***Book Management***")
        print("\nPlease select an option:")
        print("1. Show all books")
        print("2. Add a new book")
        print("3. Return to main menu")
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
            return menu()
        else:
            print("Invalid choice")

def team_operations():
    while True:
        print("\n***Team Management***")
        print("\nPlease select an option:")
        print("1. Create a new team")
        print("2. Show all teams")
        print("3. Show a single team")
        print("4. Edit a team")
        print("5. Delete a team")
        print("6. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            name = input("Enter team name: ")
            stadium = input("Enter stadium name: ")
            Teams.create_team(name, stadium)
            print(f"{name} has been registered successfully!")
        elif choice == "2":
            print(Teams.show_all_teams())
        elif choice == "3":
            team_id = input("Enter team id: ")
            team = Teams.show_single_team(team_id)
            print(team)
        elif choice == "4":
            team_id = input("Enter team id: ")
            print(f"Selected Team: {Teams.show_single_team(team_id)}\n")
            name = input("Enter new team name: ")            
            Teams.edit_team(team_id, name)
            print(f"Team {team_id} has been updated successfully!")
        elif choice == "5":
            team_id = input("Enter team id: ")
            Teams.delete_team(team_id)
            print(f"Team {team_id} has been deleted successfully!")
        elif choice == "6":
            return menu()
        else:
            print("Invalid choice")

def game_operations():
    while True:
        print("\n***Game Management***")
        print("\nPlease select an option:")
        print("1. Create a new game")
        print("2. Show all games")
        print("3. Show a single game")
        print("4. Edit a game")
        print("5. Delete a game")
        print("6. Display total goals scored by a team")
        print("7. Display average goals scored by a team")
        print("8. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            home_team = input("Enter home team name: ")
            away_team = input("Enter away team name: ")
            home_score = input("Enter home team score: ")
            away_score = input("Enter away team score: ")
            stadium = input("Enter stadium name: ")
            Games.create_game(home_team, away_team, home_score, away_score, stadium)
            print("Game has been registered successfully!")
        elif choice == "2":
            print(Games.show_all_games())
        elif choice == "3":
            game_id = input("Enter game id: ")
            print(Games.show_game(game_id))
        elif choice == "4":
            game_id = input("Enter game id: ")
            print(f"Selected Game: {Games.show_game(game_id)}\n")
            home_team = input("Update Home Team: ")
            away_team = input("Update Away Team: ")
            home_score = input("Update Home Score: ")
            away_score = input("Update Away Score: ")
            stadium = input("Update Stadium: ")            
            Games.edit_game(game_id, home_team, away_team, home_score, away_score, stadium)
            print(f"Game {game_id} has been updated successfully!")
        elif choice == "5":
            game_id = input("Enter game id: ")
            Games.delete_game(game_id)
            print(f"Game {game_id} has been deleted successfully!")
        elif choice == "6":
            team_name = input("Enter team name: ")
            print(f"Total goals scored: {Games.total_goals(team_name)}")
        elif choice == "7":
            team_name = input("Enter team name: ")
            print(f"Goals per game: {Games.avg_goals(team_name)}")
        elif choice == "8":
            return menu()
        else:
            print("Invalid choice")

def location_operations():
    while True:
        print("\n***Location Management***")
        print("\nPlease select an option:")
        print("1. Create a new location")
        print("2. Show all locations")
        print("3. Display stadiums in a location")
        print("4. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            name = input("Enter location name: ")
            Locations.create_location(name)
            print(f"{name} has been registered successfully!")
        elif choice == "2":
            print(Locations.show_all_locations())
        elif choice == "3":
            location_name = input("Enter location name: ")
            print(Locations.local_stadiums(location_name))
        elif choice == "4":
            return menu()
        else:
            print("Invalid choice")

def stadium_operations():
    while True:
        print("\n***Stadium Management***")
        print("\nPlease select an option:")
        print("1. Create a new stadium")
        print("2. Show all stadiums")
        print("3. Display stadium home team")
        print("4. Display games played in stadium")
        print("5. Goals scored in stadium")
        print("6. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            name = input("Enter stadium name: ")
            location = input("Enter stadium location: ")
            Stadiums.create_stadium(name, location)
            print(f"{name} has been registered successfully in {location}!")
        elif choice == "2":
            print(Stadiums.show_all_stadiums())
        elif choice == "3":
            stadium_name = input("Enter stadium name: ")
            print(Stadiums.teams_in_stadium(stadium_name))
        elif choice == "4":
            stadium_name = input("Enter stadium name: ")
            print(Stadiums.games_in_stadium(stadium_name))
        elif choice == "5":
            stadium_name = input("Enter stadium name: ")
            print(f"Goals scored at {stadium_name}: {Stadiums.total_goals(stadium_name)}")
        elif choice == "6":
            return menu()
        else:
            print("Invalid choice")

def menu():
    print("\n***Welcome to the League!***")
    print("\nPlease select an option:")
    print("1. Team Management")
    print("2. Location Management")
    print("3. Stadium Management")
    print("4. Game Management")
    print("5. Book Management")
    print("00. Exit the program")

def exit_program():
    print("Goodbye!")
    exit()


if __name__ == "__main__":
    main()
