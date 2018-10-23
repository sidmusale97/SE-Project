import sys
import _thread
import base64
import requests
import json
import mysql.connector
import Simlutation as sim
import Elevator as elev
import time
import datetime
import database

mycursor = database.getCursor()

gate = 0
carPassed = 0

def main():
    while (True):
        ready = input("Please position your car in the correct position and click the button:\n")
        if (ready):
            plate ='3MMETU' #scanPlate()  <-- uncomment this to test
            plateVerify = input("Our camera scanned %s as your license plate. Enter 1 if this plate is correct or enter correct plate otherwise:\n" % (plate))
            if (plateVerify != '1'):
                plate = plateVerify.upper()

            query = "Select * from Users where License = '%s'" % (plate)
        
            mycursor.execute(query)
            result = mycursor.fetchone()
        
            if (result):
                (userId,_,_,name,_) = result
                handleExisting((name,userId))
            #if (parkingType == 1):

        
def scanPlate():
    #this sends request to openALPR api to recognize the plates
    pic = open('license.jpg', 'rb')
    license = pic.read()
    secretkey = 'sk_b178ee0e4723e2ddeb219a78'

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (secretkey)
    license_encode = base64.b64encode(license)
    r = requests.post(url, data = license_encode)

    res = r.json()

    plate = res['results'][0]['plate']
    return str(plate)


def openGate():
    gate = 1
    print('Gate opening...')

def closeGate():
    gate = 0
    carPassed = 0
    print('Gate closing...')

def checkResTime(reservations):
    now = datetime.datetime.now()
    
    for res in reservations:
        
        resTime = str(res[2])
        
        [year, month,temp] = resTime.split('-')
       
        [day, time] = temp.split('T')
        [hour, mins] = time.split(':')
        
        resTime = datetime.datetime(int(year), int(month), int(day), int(hour), int(mins), 0, 0)
        lateTime = resTime + datetime.timedelta(30)
        if (now >= resTime and now <= lateTime):
            return res
        

    return None

def handleExisting(userData):
    (name,userId) = userData
    print("Hello %s!\n" % (name))
    parkingType = input('Choose 1 for adhoc, 2 for reservation, 3 to exit:\n')
    if (parkingType == '1'):
        query = "SELECT * FROM ParkingSpots WHERE Occupied = '0'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if (not result):
            print('No spots available for ad hoc parking')
            return
        else:
            freespots =[]
            for freespot in result:
                print('Spot: %s' % (freespot[0]))
                freespots.append(freespot[0])
            
            choice = int(input('Please select a parking spot from the list:'))
            while (True):
                if (choice not in freespots):
                    choice = int(input('Error please choose a spot in the list. Please select a parking spot from the list:'))
                else:
                    break
            _thread.start_new_thread(elev.main, (choice,1))
            

    elif(parkingType == '2'):
        query = "SELECT * FROM Reservations WHERE userID = %s" % userId
        mycursor.execute(query)
        res = mycursor.fetchall()
        if (not res):
            print('No reservations found')
            return
        else:
            res = checkResTime(res)
            if (res == None):
                print("Your reservation is either not for today or has not started yet")
                return
            print('Please proceed ahead\n')
            openGate()
            carPassed = sim.moveCar()
            while (not carPassed):
                time.sleep(1)
            closeGate()

            resID = res[0]
            query = "UPDATE Reservations set CheckIn = '1' where idReservations = %s" % (resID)
            print(query)
            mycursor.execute(query)
            database.commit()
            _thread.start_new_thread(elev.handlePerson, (int(res[4]),2))
            
    elif (parkingType == '3'):
        return


main()