from matplotlib import pyplot as plt
import numpy as np
from math import pow
import sympy as sym


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

def deriv(f,x):

    h = 0.000000001                 #step-size
    return (f(x+h) - f(x))/h        #definition of derivative


def tangent_line(f, x_0, a, b):
    x = np.linspace(a, b, 200)
    y = f(x)
    y_0 = f(x_0)
    y_tan = deriv(f, x_0) * (x - x_0) + y_0

    # plotting
    plt.plot(x, y, 'r-')
    plt.plot(x, y_tan, 'b-')
    plt.axis([a, b, a, b])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of a function with tangent line')
    plt.show()

def ff(a, b, c, t):
    return a*np.arctan(c) + a*np.arctan(t/b - c)



def tanfunc(current,goal):
    """first argument takes in the current coordinate of the car and the second is the
     coordinate of the goal position this method will return the optimal
     trajectory"""
    CarLength = 3
    Depth =  2       #np.abs(goal.getY - current.getY)
    Length = 10     #np.abs(goal.getX - current.getX)
    Period = 5      # changes the slope of the curve, temporary**
    Deptharray = np.linspace(0,Depth,20)
    Periodarray =np.linspace(0, Period,20)
    Lengtharray = np.linspace(0,Length,20)
    Phasearray = np.linspace(1,3,10)

    for a in Deptharray:           #????
        for b in Periodarray:        #????
            for c in Phasearray:
                if a != 0 and b!= 0:
                    p1 = a - CarLength*np.cos((a*b)/(pow(b, 2)))  # Need to add x
                    #linspace that envelopes the whole car
                    #creating a tangent line
                    function = ff(a, b, c, Lengtharray)



                    #Radius = np.power(func_d)+1
                    #Radius= np.power(1+np.power(func_d,2), 3/2)/(np.absolute(func_d2))     # formula for radius of curvature
                    #if Radius.any() > 0.6981 or Radius.any() < -0.6981:
                    #   print(Radius)

                    #   break
                    plt.plot(Lengtharray, function)




current = Coordinate(0,0)
goal = Coordinate(4,2)

a=2.1
b=1.4
c=1
CarLength=3

#plt.plot(t, f(t), '--b')
plt.plot(list(makeMap().keys()),list(makeMap().values()))
#plt.show()

tanfunc(current, goal)
plt.show()