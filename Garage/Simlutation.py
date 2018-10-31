import time
import database

mycursor = database.getCursor()

def moveCar():
    time.sleep(3)
    print('Car Moving...')
    return 1

def unoccupy(spot):
    query = "update ParkingSpots set Occupied = 0 where SpotID = %d" % (spot)
    mycursor.execute(query)
    database.commit()

def occupy(spot):
    query = "update ParkingSpots set Occupied = 1 where SpotID = %d" % (spot)
    mycursor.execute(query)
    database.commit()