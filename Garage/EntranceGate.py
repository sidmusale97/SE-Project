import sys
import base64
import requests
import json
import mysql.connector
import Simlutation as sim
import Elevator as elev
import time
import datetime
import database

#f = open('log.txt', 'w')

mycursor = database.getCursor()

gate = 0
carPassed = 0

def main():

    while (True):
        ready = input("Please position your car in the correct position and click the button:\n")
        if (ready):
            plate ='7A23T6' #scanPlate()  <-- uncomment this to test
            plateVerify = input("Our camera scanned %s as your license plate. Enter 1 if this plate is correct or enter correct plate otherwise:\n" % (plate))
            if (plateVerify != '1'):
                plate = plateVerify.upper()

            query = "Select idUsers,Name from Users where License = '%s'" % (plate)
        
            mycursor.execute(query)
            result = mycursor.fetchone()
        
            if (result):
                (userId,name) = result
                handleExisting((name,userId,plate))
            else:
                handleNew(plate)
            #if (parkingType == 1):

        
def scanPlate():
    #this sends request to openALPR api to recognize the plates
    crop('license.jpg','cropped.jpg')

    pic = open('cropped.jpg', 'rb')
    
    license = pic.read()
    secretkey = 'sk_b178ee0e4723e2ddeb219a78'

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (secretkey)
    license_encode = base64.b64encode(license)
    r = requests.post(url, data = license_encode)

    res = r.json()

    plate = res['results'][0]['plate']
    return str(plate)


def openGate():
    global gate
    gate = 1

def closeGate():
    global gate
    gate = 0
    carPassed = 0

def checkResTime(reservations):
    now = datetime.datetime.now()
    
    for res in reservations:
        
        if (int(res[3])):
            continue
        resTime = str(res[2])
        
        [year, month,temp] = resTime.split('-')
       
        [day, time] = temp.split('T')
        [hour, mins] = time.split(':')
        
        resTime = datetime.datetime(int(year), int(month), int(day), int(hour), int(mins), 0, 0)
        lateTime = resTime + datetime.timedelta(minutes = 30)
        if (now >= resTime and now <= lateTime):
            query = "Update ParkingSpots set Reserved = 1 where SpotID = %d" % (res[4])
            mycursor.execute(query)
            database.commit()
            return res
    return None

def handleNew(plate):
    phone = input('Welcome New User! Please enter your phone number to receive enter/exit code')
    name = input('Please Enter you name!')
    query = "Insert into Users (Name, License, Phone) Values ('%s','%s','%s')" % (name,plate,phone)
    mycursor.execute(query)
    database.commit()
    query = "SELECT * FROM ParkingSpots WHERE Occupied = 0 and Reserved = 0"
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
    query = "Update ParkingSpots set Reserved = 1 where SpotID = %d" % (choice)
    mycursor.execute(query)
    database.commit()
    elev.handlePerson(choice,0,plate)    
    

def handleExisting(userData):
    (name,userId,plate) = userData
    print("Hello %s!\n" % (name))
    parkingType = input('Choose 1 for adhoc, 2 for reservation, 3 to exit:\n')
    if (parkingType == '1'):
        query = "SELECT * FROM ParkingSpots WHERE Occupied = 0 and Reserved = 0"
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
        query = "Update ParkingSpots set Reserved = 1 where SpotID = %d" % (choice)
        mycursor.execute(query)
        database.commit()
        elev.handlePerson(choice,0,plate)
            

    elif(parkingType == '2'):
        if (userId == None):
            print('You are not a registered user. You must register to make reservations.')
        query = "SELECT * FROM Reservations WHERE userID = %s and CheckIn = 0" % userId
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
            
            resID = res[0]
            query = "UPDATE Reservations set CheckIn = '1' where idReservations = %s" % (resID)
            mycursor.execute(query)
            database.commit()
            elev.handlePerson(int(res[4]),resID,plate)
            
    elif (parkingType == '3'):
        return

def crop(fname, save_name):
    import matplotlib.image as mpimg
    img = mpimg.imread(fname)

    mpimg.imsave(save_name, img[1200:1950, 200:1300, :])
    return

main()