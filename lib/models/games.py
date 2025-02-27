#Model 2 lives here
from config import CONN, CURSOR

class Games:
    #Creating a match
    @classmethod
    def create_game(cls, home_team, away_team, home_score, away_score, stadium):
        sql = "INSERT INTO games (home_team, away_team, home_score, away_score, stadium) VALUES (?,?,?,?,?)"
        CURSOR.execute(sql, (home_team, away_team, home_score, away_score, stadium))
        CONN.commit()

    #display all games
    @classmethod
    def show_all_games(cls):
        sql = "SELECT * FROM games"
        CURSOR.execute(sql)
        games = CURSOR.fetchall()
        return games
    
    #display single game
    @classmethod
    def show_game(cls, game_id):
        sql = "SELECT * FROM games WHERE game_id = ?"
        CURSOR.execute(sql, (game_id,))
        game = CURSOR.fetchall()
        return game

    #delete game    
    @classmethod
    def delete_game(cls, game_id):
        sql = "DELETE FROM games WHERE game_id = ?"
        CURSOR.execute(sql, (game_id,))
        CONN.commit()

    #edit game
    @classmethod    
    def edit_game(cls, game_id, home_team, away_team, home_score, away_score, stadium):
        sql = "UPDATE games SET home_team = ?, away_team = ?, home_score = ?, away_score = ?, stadium = ? WHERE game_id = ?"
        CURSOR.execute(sql, (home_team, away_team, home_score, away_score, stadium, game_id))
        CONN.commit()   

    #display total goals for a specific team
    @classmethod
    def total_goals(cls, team_name):
        sql = """
        SELECT SUM(home_score)
        FROM games
        WHERE home_team = ? 
        UNION ALL
        SELECT SUM(away_score)
        FROM games
        WHERE away_team = ?
        """
        CURSOR.execute(sql, (team_name, team_name))
        all_goals = CURSOR.fetchall()
        home_goals = int(all_goals[0][0])
        away_goals = int(all_goals[1][0])
        total_goals = home_goals + away_goals
        return total_goals
    

    #display average goals for a specific team
    @classmethod
    def avg_goals(cls, team_name):
        sql = """
        SELECT * FROM games WHERE home_team = ? UNION ALL SELECT * FROM games WHERE away_team = ?
        """
        CURSOR.execute(sql, (team_name, team_name))
        all_games = CURSOR.fetchall()
        games_played = len(all_games)
        goals_scored = Games.total_goals(team_name)
        avg_goals = goals_scored / games_played
        return avg_goals