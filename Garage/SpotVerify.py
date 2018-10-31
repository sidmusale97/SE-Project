import time
import database
import datetime
import TrafficManagement as TM
mycursor = database.getCursor()

def checkParking(spot,resID,floor,plate):
    badParkNote = False
    unoccupiedInitial = getUnoccupiedList(floor)
    while True:
        if (resID):#if reservation
            query = "SELECT SpotID FROM ParkingSpots where Floor = %d and Reserved = 1 and Occupied = 1" % (floor)
            mycursor.execute(query)
            res = mycursor.fetchone()
            if (int(res[0] != int(spot))):
                if (not badParkNote):#make sure user parks in the right spot
                    #send notification that user is in the wrong spot
                    badParkNote = True
                    print('Wrong Spot!!!')
                time.sleep(2)
                continue #continue waiting
            else:
                break       
        else:#if adhoc let user park anywhere
            #send user notification to enter exit building
            unoccupiedNow = getUnoccupiedList(floor)
            if (len(unoccupiedInitial) != len(unoccupiedNow)): #someone has parked
                spotParked = findSpotOccupied(unoccupiedInitial,unoccupiedNow)
                break
        time.sleep(3)

    query = "UPDATE ParkingSpots Set Reserved = 0 WHERE SpotID = %d" % (spot)
    mycursor.execute(query)
    database.commit()
    print("Successful parking")  
    now = datetime.datetime.now()
    query = "INSERT INTO ParkingHistory (License, StartTime) Values ('%s','%s')" % (plate,now)
    mycursor.execute(query)
    database.commit()
    return    

def getUnoccupiedList(floor):
    query = "select * from ParkingSpots where Floor = %s and Occupied = 0" %(floor) #get open parking spot list
    mycursor.execute(query)
    Spots = mycursor.fetchall()
    return Spots

def unReserve(spot):
    query = "UPDATE ParkingSpots Reserved = 0 WHERE SpotID = %d" % (spot)
    mycursor.execute(query)
    database.commit()

def findSpotOccupied(initial, final):
    finalSpotList = [None]*len(final)
    spotParked = 0
    for f in range(len(final)):
        finalSpotList[f] = final[f][0]
    for i in initial:
        if(i[0] not in finalSpotList):
            spotParked = i[0]
            break
    return spotParked