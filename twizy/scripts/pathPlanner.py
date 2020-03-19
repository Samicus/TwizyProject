from matplotlib import pyplot as plt
import numpy as np


class Coordinate:
    def __init__(self, x, y):
        """first Argument is the x coordinate and second is the y coordinate"""
        self.x = x
        self.y = y


def makeMap():  ## for now it will return a fixed map
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
        0.7: 1,
        0.8: 1,
        0.9: 1,
        1.0: 1,
        1.1: 1,
        1.2: 1,
        1.3: 1,
        1.4: 1,
        1.5: 1,
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
        6.1: 3.5,
        6.2: 3.5,
        6.3: 3.5,
        6.4: 3.5,
        6.5: 3.5,
        6.6: 3.5,
        6.7: 3.5,
        6.8: 3.5,
        6.9: 3.5,
        7.0: 3.5,
        7.1: 1.0,
        7.2: 1.0,
        7.3: 1.0,
        7.4: 1.0,
        7.5: 1.0,
        7.6: 1.0,
        7.7: 1.0,
        7.8: 1.0,
        7.9: 1.0,
        8.0: 1.0,
        8.1: 1.0,
        8.2: 1.0,
        8.3: 1.0,

    }
    return parkmap


def filter_collision(x_0, y_0, deriv):
    circleRadius = 0.01   ### OBS! Check this value!!!
    distanceList = []
    parkingmap = makeMap()
    carlength = 3                       ### OBS! Check this value!!!
    halfCar = carlength / 2
    angle = np.arctan(deriv)
    if (deriv > 0):
        p1 = Coordinate(x_0 - halfCar * np.cos(angle), y_0 - halfCar * np.sin(angle))
        p2 = Coordinate(x_0 + halfCar * np.cos(angle), y_0 + halfCar * np.sin(angle))
    else:
        p1 = Coordinate(x_0 - halfCar * np.cos(angle), y_0 + halfCar * np.sin(angle))
        p2 = Coordinate(x_0 + halfCar * np.cos(angle), y_0 - halfCar * np.sin(angle))

    tang_linspace = np.linspace(p1.x, p2.x, 20)
    tangent = deriv * (tang_linspace - x_0) + y_0
   #plt.plot(tang_linspace, tangent)            #check collision instead?
    for x in tang_linspace:
        distanceList.clear()
        for key in parkingmap:
            counter = 0
            tangent = deriv * (x- x_0) + y_0
            dist = distance(x,tangent,key,parkingmap.get(key))
            if dist < circleRadius:
                return True
    return False






def distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1) **2)


def f_arctan(a, b, c, x):
    return a * np.arctan(c) + a * np.arctan(x/b - c)


def f_arctan_d1(a, b, c, x):  # derivative of f_arctan
    return a / (b * (1 + (np.power(c - x / b, 2))))


def f_arctan_d2(a, b, c, x):  # second derivative of f_arctan
    return (2 * a * (c - x / b)) / (np.power(b, 2) * (np.power(np.power(c - x / b, 2) + 1, 2)))


def path(current, goal):
    """first argument takes in the current coordinate of the car and the second is the
     coordinate of the goal position this method will return the optimal
     trajectory"""
    CarLength = 3                                 ### OBS! Check this value!!!
    Depth = np.abs(goal.y - current.y)  # 2
    Length = np.abs(goal.x - current.x)  # 10
    Period = 10                                 ### OBS! Check this value!!!
    Deptharray = np.linspace(0, Depth, 10)
    Periodarray = np.linspace(1, Period, 10)
    Lengtharray = np.linspace(0, Length, 20)
    Phasearray = np.linspace(0, 3, 20)
    radius = []

    for a in Deptharray:
        for b in Periodarray:
            for c in Phasearray:
                if a != 0 and b != 0:
                    radius.clear()
                    collision1 = False
                    counter = 0
                    function = f_arctan(a, b, c, Lengtharray)

                    if abs((f_arctan(a, b, c,
                                     goal.x) - goal.y)) > 10:  # filter out every function of which distance to
                        break  # to the goal position at goal.x is to big

                    if f_arctan_d1(a, b, c, goal.x) > 1:  # filter out every function that ends with a slope
                        break  # larger than 0.1 rad (to ensure that the car is parked horizontally)


                    for x in Lengtharray:  # filter out every function with a radius of curvature smaller
                        if x != 0:          # than that of renault twizy
                            f_deriv = f_arctan_d1(a, b, c, x)  # first derivative
                            f_deriv2 = f_arctan_d2(a, b, c, x)  # second derivative

                            if f_deriv2 != 0:
                                radius.insert(counter,np.absolute(np.power(1 + np.power(f_deriv, 2), 3 / 2) / f_deriv2))   # formula for radius of curvature
                                counter = counter + 1

                    if min(radius) < 3.3:       # filter out every function with a radius of curvature smaller            ### OBS! Check this value
                        break  # than that of renault twizy



                    for x in Lengtharray:
                        if x != 0:
                            f_deriv = f_arctan_d1(a, b, c, x)  # first derivative
                            collision = filter_collision(x, f_arctan(a, b, c, x), f_deriv)

                            if collision == True:
                                collision1 = True

                    if collision1 == True:
                        break

                    plt.plot(Lengtharray, function)
                                  # TODO: Lägg till dessa i funktioner


current = Coordinate(0, 0)
goal = Coordinate(5, 2.25)

a = 2.5
b = 1.4
c = 1
CarLength = 3

# plt.plot(t, f(t), '--b')
plt.plot(list(makeMap().keys()), list(makeMap().values()))
# plt.show()

path(current, goal)
plt.show()
