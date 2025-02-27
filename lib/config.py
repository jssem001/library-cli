import sqlite3
CONN = sqlite3.connect('league.db')
CURSOR = CONN.cursor()

class Database:
    @classmethod
    def create_tables(cls):
        sql_teams="""
        CREATE TABLE IF NOT EXISTS teams(
        team_id INTEGER PRIMARY KEY,
        team_name varchar(40),
        stadium varchar(40), 
        FOREIGN KEY(stadium) REFERENCES stadiums(stadium_name)
        )
        """
        CURSOR.execute(sql_teams)
        CONN.commit()

        sql_games="""
        CREATE TABLE IF NOT EXISTS games(
        game_id INTEGER PRIMARY KEY,
        home_team varchar(40),
        away_team varchar(40),
        home_score INTEGER,
        away_score INTEGER,
        stadium varchar(40),
        FOREIGN KEY(home_team) REFERENCES teams(team_name)
        FOREIGN KEY(away_team) REFERENCES teams(team_name)
        FOREIGN KEY(stadium) REFERENCES stadiums(stadium_name)
        )
        """
        CURSOR.execute(sql_games)
        

        sql_stadiums="""
        CREATE TABLE IF NOT EXISTS stadiums(
        stadium_id INTEGER PRIMARY KEY,
        stadium_name varchar(40),
        location varchar(40),
        FOREIGN KEY(location) REFERENCES locations(location_name)
        )
        """
        CURSOR.execute(sql_stadiums)
        

        sql_locations="""
        CREATE TABLE IF NOT EXISTS locations(
        location_id INTEGER PRIMARY KEY,
        location_name varchar(40)
        )
        """
        CURSOR.execute(sql_locations)
        
        CONN.commit()

    @classmethod
    def drop_tables(cls):
        sql_teams="""
        DROP TABLE IF EXISTS teams
        """
        CURSOR.execute(sql_teams)
        
        sql_games="""
        DROP TABLE IF EXISTS games
        """
        CURSOR.execute(sql_games)
        
        sql_stadiums="""
        DROP TABLE IF EXISTS stadiums
        """
        CURSOR.execute(sql_stadiums)
        
        sql_locations="""
        DROP TABLE IF EXISTS locations
        """
        CURSOR.execute(sql_locations)
        
        CONN.commit()
