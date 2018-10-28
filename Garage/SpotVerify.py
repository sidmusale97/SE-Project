import time
import database
import TrafficManagement as TM
mycursor = database.getCursor()

def checkParking(spot,resID,floor):
    badParkNote = False
    while True:
        query = "SELECT SpotID FROM ParkingSpots where Floor = %d and Changed = 1" % (floor)
        mycursor.execute(query)
        res = mycursor.fetchone()
        if (res):
            if (resID):#if reservation
                if (int(res[0] != int(spot))):
                    if (not badParkNote):#make sure user parks in the right spot
                        #send notification that user is in the wrong spot
                        badParkNote = True
                        print('Wrong Spot!!!')
                    continue #continue waiting
                else:
                    print("Successful res")  
                    query = "UPDATE Reservations SET CheckIn = 1 WHERE idReservations = %d" % (resID)
                    return    
            else:#if adhoc let user park anywhere
                #send user notification to enter exit building
                query = "UPDATE ParkingSpots SET Occupied = 1, Changed = 0 WHERE SpotID = %d" % (res)
                mycursor.execute(query)
                database.commit()
                TM.readyFloor(floor)
                print('successful adhoc')
                return
    
        time.sleep(3)