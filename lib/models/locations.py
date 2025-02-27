#model 3 lives here.
from config import CONN, CURSOR

class Locations:
    #create location    
    @classmethod    
    def create_location(cls, location_name):
        sql = "INSERT INTO locations (location_name) VALUES (?)"
        CURSOR.execute(sql, (location_name,))
        CONN.commit()
    
    #show all locations
    @classmethod
    def show_all_locations(cls):
        sql = "SELECT * FROM locations"
        CURSOR.execute(sql)
        locations = CURSOR.fetchall()
        return locations
    
    #show stadiums in a location
    @classmethod
    def local_stadiums(cls, location_name):
        sql = "SELECT * FROM stadiums WHERE location = ?"
        CURSOR.execute(sql, (location_name,))
        stadiums = CURSOR.fetchall()
        return stadiums