#model 3 lives here.
from config import CONN, CURSOR  

class Stadiums:
    @classmethod
    def create_stadium(cls, stadium_name, location):
        sql = "INSERT INTO stadiums (stadium_name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (stadium_name, location))
        CONN.commit()

    #show all stadiums
    @classmethod
    def show_all_stadiums(cls):
        sql = "SELECT * FROM stadiums"
        CURSOR.execute(sql)
        stadiums = CURSOR.fetchall()
        return stadiums
    
    #show all games in a stadium
    @classmethod
    def games_in_stadium(cls, stadium_id):
        sql = "SELECT * FROM games WHERE stadium = ?"
        CURSOR.execute(sql, (stadium_id,))
        games = CURSOR.fetchall()
        return games
    
    #show team that plays in a stadium
    @classmethod
    def teams_in_stadium(cls, stadium_name):
        sql = "SELECT * FROM teams WHERE stadium = ?"
        CURSOR.execute(sql, (stadium_name,))
        team = CURSOR.fetchall()
        return team
    
    #display total goals for a specific stadium
    @classmethod
    def total_goals(cls, stadium_name):
        sql = """
        SELECT SUM(home_score + away_score)
        FROM games
        WHERE stadium = ? 
        """
        CURSOR.execute(sql, (stadium_name,))
        all_goals = CURSOR.fetchone()[0]
        return all_goals