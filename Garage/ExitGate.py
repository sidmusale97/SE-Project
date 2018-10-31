import requests
import datetime
import json
import base64
import database
import mysql.connector
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
  elapsed_time = current_time - park_start_time
  hours = round(elapsed_time.total_seconds()/3600.00*100)/100.0
  return park_start_time,current_time,hours
  #print(park_start_time)
  #print(current_time)
  #print(hours)


def test():
  plateid="W92HSD"   #scanPlate()
  print('plate id=',plateid)

if __name__ == "__main__":
  test()
  get_datetime_hours("W92HSD")

