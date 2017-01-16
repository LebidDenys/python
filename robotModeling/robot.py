import math
import random
import robot_visualize
import pylab
import numpy as np
from robot_verify_movement27 import testRobotMovement

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x, self.y = x, y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        """
        if width <= 0 or height <= 0:
            raise IncorrectEnterredValuesError

        self.width = int(width)
        self.height = int(height)
        self.area = self.height*self.width

        self.tilesList = {}
        for i in range(width):
            for j in range(height):
                self.tilesList[i,j] = 'dirty'

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        """
        self.tilesList[int(math.floor(pos.x)), int(math.floor(pos.y))] = 'clean'

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        """
        return self.tilesList[m, n] == 'clean'

    def getNumTiles(self):
        return len(self.tilesList)

    def getNumCleanedTiles(self):
        return len([value for value in self.tilesList.values() if value =='clean'])

    def getRandomPosition(self):
        return Position(random.uniform(0, self.width-1), random.uniform(0, self.height-1))

    def isPositionInRoom(self, pos):
        return (int(math.floor(pos.x)), int(math.floor(pos.y))) in self.tilesList.keys()


class Robot(object):
    """
    Represents a robot cleaning a particular room.
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
    """
    def __init__(self, room, speed):
        self.room = room
        self.position = self.room.getRandomPosition()
        self.direction = random.randrange(1, 360, 1)
        self.speed = speed

        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        return self.position

    def getRobotDirection(self):
        return self.direction

    def setRobotPosition(self, position):
        self.position = position

    def setRobotDirection(self, direction):
        self.direction = direction


class StandardRobot(Robot):

    def __init__(self, room, speed):
        Robot.__init__(self, room, speed)

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        """
        if self.room.isPositionInRoom(self.position.getNewPosition(self.direction, self.speed)):
            self.position = self.position.getNewPosition(self.direction, self.speed)
            self.room.cleanTileAtPosition(self.position)
        else:
            self.setRobotDirection(random.randrange(1, 360, 1))


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.
    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    """
    mean = 0
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robots = [robot_type(room, speed) for i in range(num_robots)]
        min_tiles = min_coverage * room.getNumTiles()
        time_steps = 0
        while min_tiles != room.getNumCleanedTiles():
            anim.update(room, robots)
            map(lambda x: x.updatePositionAndClean(),robots)
            time_steps += 1
        mean += time_steps
        anim.done()
    return mean/num_trials


class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def __init__(self, room, speed):
        Robot.__init__(self, room, speed)

    def updatePositionAndClean(self):
        self.setRobotDirection(random.randrange(1, 360, 1))
        if self.room.isPositionInRoom(self.position.getNewPosition(self.getRobotDirection(), self.speed)):
            self.room.cleanTileAtPosition(self.position)
            self.setRobotPosition(self.position.getNewPosition(self.getRobotDirection(), self.speed))


anim = robot_visualize.RobotVisualization(10, 10, 15)
runSimulation(10, 1.0, 10, 15, 0.8, 30, StandardRobot)

def showPlot1(title, x_label, y_label):
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

def showPlot2(title, x_label, y_label):
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room ', 'Number of Robots', 'Time-steps')

showPlot2('Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms ','Aspect Ratio','Time-steps')
