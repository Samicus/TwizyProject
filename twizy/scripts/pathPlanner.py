from matplotlib import pyplot as plt
import numpy as np
from math import pow
import sympy as sym


class Coordinate:
    def __init__(self,x,y):
      """first Argument is the x coordinate and second is the y coordinate"""
      self.x = x
      self.y = y


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
        0.7: 3.5,
        0.8: 3.5,
        0.9: 3.5,
        1.0: 3.5,
        1.1: 3.5,
        1.2: 3.5,
        1.3: 3.5,
        1.4: 3.5,
        1.5: 3.5,
        1.6: 3.5,
        1.7: 3.5,
        1.8: 3.5,
        1.9: 3.5,
        2.0: 3.5,
        2.1: 3.5,
        2.2: 3.5,
        2.3: 3.5,
        2.5: 3.5,
        2.6: 3.5,
        2.7: 3.5,
        2.8: 3.5,
        2.9: 3.5,
        3.0: 3.5,
        3.1: 3.5,
        3.2: 3.5,
        3.3: 3.5,
        3.4: 3.5,
        3.5: 3.5,
        3.6: 3.5,
        3.7: 3.5,
        3.8: 3.5,
        3.9: 3.5,
        4.0: 3.5,
        4.1: 3.5,
        4.2: 3.5,
        4.3: 3.5,
        4.4: 3.5,
        4.5: 3.5,
        4.6: 3.5,
        4.7: 3.5,
        4.8: 3.5,
        4.9: 3.5,
        5.0: 3.5,
        5.1: 3.5,
        5.2: 3.5,
        5.3: 3.5,
        5.4: 3.5,
        5.5: 3.5,
        5.6: 3.5,
        5.7: 3.5,
        5.8: 3.5,
        5.9: 3.5,
        6.0: 3.5,
        6.1: 1.0,
        6.2: 1.0,
        6.3: 1.0,
        6.4: 1.0,
        6.5: 1.0,
        6.6: 1.0,
        6.7: 1.0,
        6.8: 1.0,
        6.9: 1.0,
        7.0: 1.0,
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

def f_arctan(a, b, c, x):
    return a*np.arctan(c) + a*np.arctan(x/b - c)


def f_arctan_d1(a, b, c, x):        #derivative of f_arctan
    return a/(b*(1+(np.power(c-x/b,2))))


def f_arctan_d2(a, b, c, x):        #second derivative of f_arctan
    return (2*a*(c-x/b)) / (np.power(b,2)*(np.power(np.power(c-x/b,2)+1,2)))


def path(current,goal):
    """first argument takes in the current coordinate of the car and the second is the
     coordinate of the goal position this method will return the optimal
     trajectory"""
    CarLength = 3
    Depth =  np.abs(goal.y - current.y)    #2
    Length = np.abs(goal.x - current.y)      #10
    Period = 7      # changes the slope of the curve, temporary**
    Deptharray = np.linspace(0,Depth,20)
    Periodarray =np.linspace(0, Period,20)
    Lengtharray = np.linspace(0,Length,20)
    Phasearray = np.linspace(1,5,20)

    for a in Deptharray:           #????
        for b in Periodarray:        #????
            for c in Phasearray:
                if a != 0 and b!= 0:
                    function= f_arctan(a, b, c, Lengtharray)

                    if abs((f_arctan(a, b, c, goal.x) - goal.y)) > 0.2:   # filter out every function of which distance to
                        break                                             # to the goal position at goal.x is to big

                    if f_arctan_d1(a, b, c, goal.x ) > 0.1:               # filter out every function that ends with a slope
                        break                                             # larger than 0.1 rad (to ensure that the car is parked horizontally)
                    for x in Lengtharray:       # filter out every function with a radius of curvature larger
                       if x != 0:               # than that of renault twizy

                           f_deriv = f_arctan_d1(a, b, c, x)        # first derivative
                           f_deriv2 = f_arctan_d2(a, b, c, x)       # second derivative

                           if f_deriv2 != 0:
                               Radius= int(np.absolute(np.power(1+np.power(f_deriv, 2), 3/2)/((f_deriv2))))  #formula for radius of curvature
                               if Radius < 3.3:
                                  plt.plot(Lengtharray, function)
                                  #TODO: Lägg till dessa i funktioner








current = Coordinate(0,0)
goal = Coordinate(5, 2.25)

a=2.5
b=1.4
c=1
CarLength=3

#plt.plot(t, f(t), '--b')
plt.plot(list(makeMap().keys()),list(makeMap().values()))
#plt.show()
 
path(current, goal)
plt.show()