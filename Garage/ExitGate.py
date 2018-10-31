import requests
import datetime
import json
import base64
import database
import mysql.connector
import billing as bill
mycursor = database.getCursor()

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

def get_datetime_hours(license_plate):
    query = "select * from ParkingHistory where License='%s'" % license_plate
    mycursor.execute(query)
    res=mycursor.fetchone()
    park_start_time = res[1]
    current_time = datetime.datetime.now()
    query = "Update ParkingHistory Set EndTime = '%s', Paid = 1 where License = '%s' and EndTime = ''" % (current_time,license_plate)
    mycursor.execute(query)
    database.commit()
    elapsed_time = current_time - park_start_time
    hours = round(elapsed_time.total_seconds()/3600.00*100)/100.0
    return hours
    #print(park_start_time)
    #print(current_time)
    #print(hours)


def main():
    while (True):
        ready = input("Please position your car in the correct position and click the button:\n")
        if (ready):
            plate ='7A23T6' #scanPlate()  <-- uncomment this to test
            plateVerify = input("Our camera scanned %s as your license plate. Enter 1 if this plate is correct or enter correct plate otherwise:\n" % (plate))
            if (plateVerify != '1'):
                plate = plateVerify.upper()
            hours = get_datetime_hours(plate)
            query = "select Name,Email From Users where License = '%s'" % (plate)
            mycursor.execute(query)
            (Name,Email)=mycursor.fetchone()
            if (not Email):
                Email = input("Hello %s! Please enter your email to receive digital receipt"% (Name)) 
            bill.email(Name,Email,hours)
            print('Thank you for parking with us. Please check your Email for your receipt')

main()



