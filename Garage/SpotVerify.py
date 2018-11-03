import time
import database
import datetime
import TrafficManagement as TM
import Notifications as noti
mycursor = database.getCursor()

def checkParking(spot,resID,floor,plate):
    badParkNote = False
    unoccupiedInitial = getUnoccupiedList(floor)
    phone = getPhonefromPlate(plate)
    while True:
        unoccupiedNow = getUnoccupiedList(floor)
        if (len(unoccupiedInitial) != len(unoccupiedNow)): #someone has parked
            spotParked = findSpotOccupied(unoccupiedInitial,unoccupiedNow)
            if (resID):#if reservation
                if (int(spotParked != int(spot))):
                    if (not badParkNote):#make sure user parks in the right spot
                        #send notification that user is in the wrong spot
                        badParkNote = True
                        noti.sendWrongSpot(phone,spot)
                    time.sleep(2)
                    continue #continue waiting
                else:
                    break       
            else:
                break
        time.sleep(3)

    unReserve(spot)
    print("Successful parking")  
    TM.readyFloor(floor)
    phone = getPhonefromPlate(plate)
    noti.sendAuth(phone)      # need to move this to spotverify later, just adding here for quick merge
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
    query = "UPDATE ParkingSpots Set Reserved = 0 WHERE SpotID = %d" % (spot)
    mycursor.execute(query)
    database.commit()

def findSpotOccupied(initial, final):#finds newly occupied spot based on intial and final state
    finalSpotList = [None]*len(final)
    spotParked = 0
    for f in range(len(final)):
        finalSpotList[f] = final[f][0]#insert all occupied spots into spot list
    for i in initial:
        if(i[0] not in finalSpotList):#if spot is in initial state list and not in final then it is occupied
            spotParked = i[0]
            break
    return spotParked

def getPhonefromPlate(plate):
    query = "Select Phone From Users Where License = '%s'"  % (plate)
    mycursor.execute(query)
    phone = mycursor.fetchone()
    phone = phone[0]
    return phone