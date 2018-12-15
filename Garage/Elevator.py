'''
written by: Siddharth Musale
tested by: Siddharth Musale
debugged by: Siddharth Musale
'''
import time
import TrafficManagement as TM
import SpotVerify as verify
import Simlutation as sim
import _thread
import Notifications as noti


def handlePerson(spot,resID,plate):
    #extract floor from spot number
    floor = int(spot/100)

    #check if floor is ready to parked on
    while(not TM.isFloorReady(floor)):
        time.sleep(1) #wait until floor is ready
    
    TM.unreadyFloor(floor) #once floor becomes availiable make it unavailiable as the next person has begun parking
    bringCar(floor,spot,resID,plate) #commence elevator 
    


def bringCar(floor,spot,resID,plate):
     #messages for debugging
    print("going to floor %d" % (floor))
    time.sleep(1)
    print("on floor %d" % (floor))
    time.sleep(1)

    #spawn new thread to verify spot parking
    _thread.start_new_thread(verify.checkParking, (spot,resID,floor,plate))
    time.sleep(2)
    print('Returning to floor 1')
    time.sleep(1)
    print('At floor 1')
