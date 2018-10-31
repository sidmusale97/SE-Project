import time
import TrafficManagement as TM
import SpotVerify as verify
import Simlutation as sim
import _thread
import Notifications as noti

tempPhone = "+19739347753"      # set this to the number you want to send a text to (need to automate per user later)

def handlePerson(spot,resID,plate):
    floor = int(spot/100)
    while(not TM.isFloorReady(floor)):
        time.sleep(1)
    TM.unreadyFloor(floor)
    bringCar(floor,spot,resID,plate)  
    


def bringCar(floor,spot,resID,plate):
    print("going to floor %d" % (floor))
    time.sleep(1)
    print("on floor %d" % (floor))
    time.sleep(1)
    _thread.start_new_thread(verify.checkParking, (spot,resID,floor,plate))
    time.sleep(2)
    print('Returning to floor 1')
    time.sleep(1)
    print('At floor 1')
