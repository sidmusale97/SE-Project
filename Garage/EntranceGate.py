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


mydb = mysql.connector.connect(
    host = 'se-project.cqeckwiwnfhm.us-east-2.rds.amazonaws.com',
    user = 'root',
    passwd = '12345678',
    database = 'se'
)

mycursor = mydb.cursor()
gate = 0
carPassed = 0

def main():
    while (True):
        ready = input("Please position your car in the correct position and click the button:\n")
        if (ready):
            plate = #scanPlate()  <-- uncomment this to test
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
    today = (now.year,now.month,now.day)
    currentTime = (now.hour, now.minute)
    currentTime = "%d:%d" % (now.hour,now.minute)
    print(currentTime)
    for res in reservations:
        resTime = str(res[2])
        
        resTime = resTime.split('-')
       
        [day, time] = resTime[2].split('T')
        resTime.remove(resTime[2])
        resTime.append(day)
        resTime.append(time)
        

    return 0

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
                print('Spot: %s \t Floor: %s' % (freespot[0],freespot[2]))
                freespots.append(freespot[0])
            
            choice = int(input('Please select a parking spot from the list:'))
            while (True):
                if (choice not in freespots):
                    choice = int(input('Error please choose a spot in the list. Please select a parking spot from the list:'))
                else:
                    break

    elif(parkingType == '2'):
        query = "SELECT * FROM Reservations WHERE userID = %s" % userId
        mycursor.execute(query)
        res = mycursor.fetchall()
        if (not res):
            print('No reservations found')
            return
        else:
            index = checkResTime(res)

            print('Please proceed ahead\n')
            openGate()
            carPassed = sim.moveCar()
            while (not carPassed):
                time.sleep(1)
            closeGate()
            _thread.start_new_thread(elev.handlePerson, (choice,parkingType))
            



    elif (parkingType == '3'):
        return


main()