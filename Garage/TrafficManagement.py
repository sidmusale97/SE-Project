floorsReady = [True,True,True,True,True]

def isFloorReady(floor):
    global floorsReady
    return floorsReady[floor-1]

def readyFloor(floor):
    global floorsReady
    floorsReady[floor-1] = True

def unreadyFloor(floor):
    global floorsReady
    floorsReady[floor-1] = False

