#Model 1 should live here
from config import CONN, CURSOR

class Teams:
    #add a team
    @classmethod
    def create_team(cls, team_name, stadium):
        sql = "INSERT INTO teams (team_name, stadium) VALUES (?,?)"
        CURSOR.execute(sql, (team_name,stadium))
        CONN.commit()

    #show all teams
    @classmethod
    def show_all_teams(cls):
        sql = "SELECT * FROM teams"
        CURSOR.execute(sql)
        teams = CURSOR.fetchall()
        return teams
    
    #show single team
    @classmethod
    def show_single_team(cls, team_id):
        sql = "SELECT * FROM teams WHERE team_id = ?"
        CURSOR.execute(sql, (team_id,))
        team = CURSOR.fetchall()
        return team
    
    #edit team
    @classmethod
    def edit_team(cls, team_id, team_name):
        sql = "UPDATE teams SET team_name = ? WHERE team_id = ?"
        CURSOR.execute(sql, (team_name, team_id))
        CONN.commit()

    #delete team
    @classmethod
    def delete_team(cls, team_id):
        sql = "DELETE FROM teams WHERE team_id = ?"
        CURSOR.execute(sql, (team_id,))
        CONN.commit()