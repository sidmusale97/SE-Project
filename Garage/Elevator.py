import time
import TrafficManagement as TM
import SpotVerify as verify
import Simlutation as sim
import _thread

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
    print('Returning to floor 1')
    time.sleep(1)
    print('At floor 1')
