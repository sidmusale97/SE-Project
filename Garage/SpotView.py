import mysql.connector
import database

mycursor = database.getCursor()

# lists all spots in the database and their current status
def listAllSpots():
    query = "SELECT * FROM ParkingSpots"
    mycursor.execute(query)
    result = mycursor.fetchall()
    spots = []
    for spot in result:
            if spot[1] == 1:
                print('Spot: %s (occupied)' % (spot[0]))
                spots.append(spot[0])
            elif spot[2] == 1:
                print('Spot: %s (reserved)' % (spot[0]))
                spots.append(spot[0])
            else:
                print('Spot: %s' % (spot[0]))
                spots.append(spot[0])
            
listAllSpots()
