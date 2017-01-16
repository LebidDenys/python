from robot import *

# P1 - test path

# P1 Test1-1
try:
    room = RectangularRoom(5, 5)
    numTiles = room.getNumTiles()
except:
    print "Error of function - Test1"
else:    
    if numTiles == 25:
        print "Test1-1 Successfully created a room of size " + str(room.getNumTiles())
    else:
        print "Error - Test1-1 - Incorrect number of tilis"

# P1 Test1-2
try:
    room = RectangularRoom(5, 3)
    room = RectangularRoom(8, 8)
    room = RectangularRoom(6, 5)
    room = RectangularRoom(2, 6)
    room = RectangularRoom(7, 1)
    numTiles = room.getNumTiles()
except:
    print "Error of function - Test1"
else:    
    if numTiles == 7:
        print "Test1-2 Successfully created a room of size " + str(room.getNumTiles())
    else:
        print "Error - Test1-2 - Incorrect number of tilis"
