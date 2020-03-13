from matplotlib import pyplot as plt
import numpy as np
from math import pow

class Coordinate:
    def __init__(self,x,y):
      """first Argument is the x coordinate and second is the y coordinate"""
      self.x = x
      self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def makeMap():      ## for now it will return a fixed map
    """This method creates a dictionary by combining the GPS-coordinate and
     the ultrasonic sensors"""
    parkmap = {
        0.0: 1,
        0.1: 1,
        0.2: 1,
        0.3: 1,
        0.4: 1,
        0.5: 1,
        0.6: 1,
        0.7: 2,
        0.8: 2,
        0.9: 2,
        1.0: 2,
        1.1: 2,
        1.2: 2,
        1.3: 2,
        1.4: 2,
        1.5: 2,
        1.6: 2,
        1.7: 2,
        1.8: 2,
        1.9: 2,
        2.0: 2,
        2.1: 2,
        2.2: 2,
        2.3: 2,
        2.5: 2,
        2.6: 2,
        2.7: 2,
        2.8: 2,
        2.9: 2,
        3.0: 2,
        3.1: 2,
        3.2: 2,
        3.3: 2,
        3.4: 2,
        3.5: 1,
        3.6: 1,
        3.7: 1,
        3.8: 1,
        3.9: 1,
        4.0: 1
    }
    return parkmap


def f(a, b, t):
    return a*np.arctan(t/b)

def tanfunc(current,goal):
    """first argument takes in the current coordinate of the car and the second is the
     coordinate of the goal position this method will return the optimal
     trajectory"""
    CarLength = 2.737
    Depth =  2       #np.abs(goal.getY - current.getY)
    Length = 10     #np.abs(goal.getX - current.getX)
    Period = 2      # changes the slope of the curve, temporary**
    Deptharray = np.linspace(0,Depth,10)
    Periodarray =np.linspace(0, Period,10)
    Lengtharray = np.linspace(-10,Length,10)

    for a in Deptharray:           #????
        for b in Periodarray:        #????
            if a != 0 and b!= 0:
                function = f(a, b, Lengtharray)
                # p1 = a - CarLength*np.cos((a*b)/(pow(b, 2)))  #calculate how long in x direction the car reaches
                 #tangArray = (p1,a,20)                         #linspace that envelopes the whole car
                 #tangent = (a*b)/(pow(b, 2)*tangArray+1)       #creating a tangent line
                plt.plot(Lengtharray, f(a, b, Lengtharray))




current = Coordinate(0,0)
goal = Coordinate(4,2)


t = np.arange(-5, 5.0, 0.1)
#plt.plot(t, f(t), '--b')
#plt.plot(list(makeMap().keys()),list(makeMap().values()))
#plt.show()

tanfunc(current, goal)
plt.show()