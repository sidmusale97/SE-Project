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
        #simulate customer clicking a button when they arrive to the garage
        ready = input("Please position your car in the correct position and click the button:\n")
        if (ready):
            plate =scanPlate()
            #allow user to change the plate if the camera detected the wrong license plate
            plateVerify = input("Our camera scanned %s as your license plate. Enter 1 if this plate is correct or enter correct plate otherwise:\n" % (plate))
            if (plateVerify != '1'):
                plate = plateVerify.upper()#normalize all plates to upper case

            #query database for user that has this license plate associated with the account
            query = "Select idUsers,Name from Users where License = '%s'" % (plate)
            mycursor.execute(query)
            result = mycursor.fetchone()

            #if account exists then call handleExisting
            if (result):
                (userId,name) = result
                handleExisting((name,userId,plate))
            else:
                #if account DNE then handle New user
                handleNew(plate)

        
def scanPlate(): #this function reads license.jpg in the garage folder and recognizes the plate and returns the plate as a string
    #this sends request to openALPR api to recognize the plates
    crop('license.jpg','cropped.jpg')#zooms into license plate (beta)

    pic = open('license.jpg', 'rb')
    
    license = pic.read()
    secretkey = 'sk_b178ee0e4723e2ddeb219a78'

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (secretkey)
    license_encode = base64.b64encode(license)
    r = requests.post(url, data = license_encode)

    #get API response as json object
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

#return reservation that is for the current day and time takes in reservations as tuple (resID, userID, DateTime, Checkin, Parking Spot)
def checkResTime(reservations):
    #get current time
    now = datetime.datetime.now()
    
    #loop thru all reservations
    for res in reservations:
        
        #if reservation has already been checked into ie person already entered the garage
        if (int(res[3])):
            continue
        #extract time of reservation from reservation tuple
        resTime = str(res[2])
        
        [year, month,temp] = resTime.split('-')
       
        [day, time] = temp.split('T')
        [hour, mins] = time.split(':')
        
        #create datetime object for the reservation time on the database
        resTime = datetime.datetime(int(year), int(month), int(day), int(hour), int(mins), 0, 0)

        #calculate the lastest time for a customer to arrive to be able to check into the reservation
        lateTime = resTime + datetime.timedelta(minutes = 30)

        #if customer arrives within 30 mins of the start then checkin is successful
        if (now >= resTime and now <= lateTime):
            #update database for Reservation Check in
            query = "Update ParkingSpots set Reserved = 1 where SpotID = %d" % (res[4])
            mycursor.execute(query)
            database.commit()
            return res
    return None

def handleNew(plate):#takes in user data and sets up adhoc parking
    #take new user minimum data
    phone = input('Welcome New User! Please enter your phone number to receive enter/exit code')
    name = input('Please Enter you name!')

    #insert min data into database
    query = "Insert into Users (Name, License, Phone) Values ('%s','%s','%s')" % (name,plate,phone)
    mycursor.execute(query)
    database.commit()

    #Get all free spots
    query = "SELECT * FROM ParkingSpots WHERE Occupied = 0 and Reserved = 0"
    mycursor.execute(query)
    result = mycursor.fetchall()
    if (not result):
        print('No spots available for ad hoc parking')
        return
    else:
        #collect all free spots and print them
        freespots =[]
        for freespot in result:
            print('Spot: %s' % (freespot[0]))
            freespots.append(freespot[0])
        #have user select an adhoc parking spot
        choice = int(input('Please select a parking spot from the list:'))
        while (True):
            if (choice not in freespots):
                choice = int(input('Error please choose a spot in the list. Please select a parking spot from the list:'))
            else:
                break
    #reserve parking spot 
    query = "Update ParkingSpots set Reserved = 1 where SpotID = %d" % (choice)
    mycursor.execute(query)
    database.commit()
    elev.handlePerson(choice,0,plate)    
    

def handleExisting(userData):
    (name,userId,plate) = userData
    print("Hello %s!\n" % (name))
    #reservation handling
    #query database for all user reservations
    query = "SELECT * FROM Reservations WHERE userID = %s and CheckIn = 0" % userId
    mycursor.execute(query)
    res = mycursor.fetchall()
    if(res):
        #extract resID from reservation tuple
        resID = res[0]

        #update database to show that reservation has been checked into
        query = "UPDATE Reservations set CheckIn = '1' where idReservations = %s" % (resID)

        mycursor.execute(query)
        database.commit()
        elev.handlePerson(int(res[4]),resID,plate)
        print("Your reservation for %s is checked in" % res[2])
        return
    #allow registered users to choose parking type
    parkingType = input('Choose 1 for adhoc, 3 to exit:\n')
    if (parkingType == '1'):
        query = "SELECT * FROM ParkingSpots WHERE Occupied = 0 and Reserved = 0"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if (not result):
            print('No spots available for ad hoc parking')
            return
        else:
            #display parking spots
            freespots =[]
            for freespot in result:
                print('Spot: %s' % (freespot[0]))
                freespots.append(freespot[0])
            #take in user spot choice
            choice = int(input('Please select a parking spot from the list:'))
            while (True):
                if (choice not in freespots):
                    choice = int(input('Error please choose a spot in the list. Please select a parking spot from the list:'))
                else:
                    break
        #reserve selected spot
        query = "Update ParkingSpots set Reserved = 1 where SpotID = %d" % (choice)
        mycursor.execute(query)
        database.commit()
        elev.handlePerson(choice,0,plate)
                
    elif (parkingType == '3'):
        return

#zooms into lower part of picture (beta)
def crop(fname, save_name):
    import matplotlib.image as mpimg
    img = mpimg.imread(fname)

    mpimg.imsave(save_name, img[1200:1950, 200:1300, :])
    return

main()