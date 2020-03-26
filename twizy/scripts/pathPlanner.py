from matplotlib import pyplot as plt
import numpy as np


class Coordinate:
    def __init__(self, x, y):
        """first Argument is the x coordinate and second is the y coordinate"""
        self.x = x
        self.y = y

        # mapa avstånd på parkering, avstånd till bilen i slutet och göra en map
        # utifrån det. ---- Ta in Parkeringslängd, avstånd till bilen bredvid,(och längden ifrån parkeringen?)


# Python3 program to Convert a
# list to dictionary

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


def makeMap():  ## for now it will return a fixed map
    """This method creates a dictionary by combining the GPS-coordinate and
     the ultrasonic sensors"""


    parkmap = {
        0.0: distance,
        0.1: distance,
        0.2: distance,
        0.3: distance,
        0.4: distance,
        0.5: distance,
        0.6: distance,
        0.7: distance,
        0.8: distance,
        0.9: distance,
        1.0: distance,
        1.1: distance,
        1.2: distance,
        1.3: distance,
        1.4: distance,
        1.5: distance,
        1.51: 0.3 + distance,
        1.52: 0.5 + distance,
        1.53: 0.9 + distance,
        1.54: 1.1 + distance,
        1.55: 1.4 + distance,
        1.56: 1.7 + distance,
        1.57: 2.0 + distance,  ## Higher density needed here!
        1.58: 2.25 + distance,
        1.59: 2.4  + distance,
        1.6: distance + 2.5,
        1.7: distance + 2.5,
        1.8: distance + 2.5,
        1.9: distance + 2.5,
        2.0: distance + 2.5,
        2.1: distance + 2.5,
        2.2: distance + 2.5,
        2.3: distance + 2.5,
        2.5: distance + 2.5,
        2.6: distance + 2.5,
        2.7: distance + 2.5,
        2.8: distance + 2.5,
        2.9: distance + 2.5,
        3.0: distance + 2.5,
        3.1: distance + 2.5,
        3.2: distance + 2.5,
        3.3: distance + 2.5,
        3.4: distance + 2.5,
        3.5: distance + 2.5,
        3.6: distance + 2.5,
        3.7: distance + 2.5,
        3.8: distance + 2.5,
        3.9: distance + 2.5,
        4.0: distance + 2.5,
        4.1: distance + 2.5,
        4.2: distance + 2.5,
        4.3: distance + 2.5,
        4.4: distance + 2.5,
        4.5: distance + 2.5,
        4.6: distance + 2.5,
        4.7: distance + 2.5,
        4.8: distance + 2.5,
        4.9: distance + 2.5,
        5.0: distance + 2.5,
        5.1: distance + 2.5,
        5.2: distance + 2.5,
        5.3: distance + 2.5,
        5.4: distance + 2.5,
        5.5: distance + 2.5,
        5.6: distance + 2.5,
        5.7: distance + 2.5,
        5.8: distance + 2.5,
        5.9: distance + 2.5,
        6.0: distance + 2.5,
        6.1: distance + 2.5,
        6.2: distance + 2.5,
        6.3: distance + 2.5,
        6.4: distance + 2.5,
        6.5: distance + 2.5,
        6.6: distance + 2.5,
        6.7: distance + 2.5,
        6.8: distance + 2.5,
        6.9: distance + 2.5,
        7.0: distance + 2.5,
        7.1: distance,
        7.2: distance,
        7.3: distance,
        7.4: distance,
        7.5: distance,
        7.6: distance,
        7.7: distance,
        7.8: distance,
        7.9: distance,
        8.0: distance,
        8.1: distance,
        8.2: distance,
        8.3: distance,

    }
    return parkmap


def filter_collision(x_0, y_0, deriv):
    circleRadius = 0.69  ### OBS! Check this value!!!
    parkingmap = makeMap()
    carlength = 2.32  ### OBS! Check this value!!!
    halfCar = carlength / 2
    angle = np.arctan(deriv)
    counter = 0
    if (deriv > 0):
        p1 = Coordinate(x_0 - halfCar * np.cos(angle), y_0 - halfCar * np.sin(angle))
        p2 = Coordinate(x_0 + halfCar * np.cos(angle), y_0 + halfCar * np.sin(angle))
    else:
        p1 = Coordinate(x_0 - halfCar * np.cos(angle), y_0 + halfCar * np.sin(angle))
        p2 = Coordinate(x_0 + halfCar * np.cos(angle), y_0 - halfCar * np.sin(angle))

    tang_linspace = np.linspace(p1.x, p2.x, 20)
    #tangent = deriv * (tang_linspace - x_0) + y_0
    #plt.plot(tang_linspace, tangent)            #check collision instead?
    for x in tang_linspace:
        counter = counter + 1
        if counter > 6 or counter < 16:
            for key in parkingmap:
                tangent = deriv * (x - x_0) + y_0
                dist = distance1(x, tangent, key, parkingmap.get(key))
                if dist < circleRadius:
                    return True
    return False


def distance1(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def f_arctan(a, b, c, x):
    return a * np.arctan(c / b + 3) + a * np.arctan((1 / b) * (x - 3 * b - c))


def f_arctan_d1(a, b, c, x):  # derivative
    # return a / (b * (1 + (np.power(c - x / b, 2))))
    return a / (b * (np.power(x - 3 * b - c, 2) / np.power(b, 2) + 1))


def f_arctan_d2(a, b, c, x):  # second derivative
    # return (2 * a * (c - x / b)) / (np.power(b, 2) * (np.power(np.power(c - x / b, 2) + 1 , 2)))
    return (2 * a * (-3 * b - c + x)) / (np.power(b, 3) * np.power(np.power(-3 * b - c + x, 2) / np.power(b, 2) + 1 , 2))


def path(current, goal):
    """first argument takes in the current coordinate of the car and the second is the
     coordinate of the goal position this method will return the optimal
     trajectory"""
    depth = np.abs(goal.y - current.y)  # 2
    length = np.abs(goal.x - current.x)  # 10
    period = 2
    phase = 100
    deptharray = np.linspace(0.5, depth/2, 30)
    periodarray = np.linspace(0, period, 20)
    lengtharray = np.linspace(current.x, current.x + length, 20)
    phasearray = np.linspace(0, phase, 20)

    radius = []
    for a in deptharray:
        for b in periodarray:
            for c in phasearray:
                if a != 0 and b != 0:
                    radius.clear()
                    collision1 = False
                    counter = 0
                    function = f_arctan(a, b, c, lengtharray)
                    #plt.plot(lengtharray,function)
                    if abs((f_arctan(a, b, c,
                                     goal.x) - goal.y)) > 0.2:  # filter out every function of which distance to
                        break                                   # to the goal position at goal.x is to big

                    if f_arctan_d1(a, b, c, goal.x) > 0.2:  # filter out every function that ends with a slope
                        break  # larger than 0.1 rad (to ensure that the car is parked horizontally)


                    for x in lengtharray:  # filter out every function with a radius of curvature smaller
                        if x != 0:  # than that of renault twizy
                            f_deriv = f_arctan_d1(a, b, c, x)  # first derivative
                            f_deriv2 = f_arctan_d2(a, b, c, x)  # second derivative

                            if f_deriv2 != 0:
                                radius.insert(counter, np.absolute(np.power(1 + np.power(f_deriv, 2),
                                                                            3 / 2) / f_deriv2))  # formula for radius of curvature
                                counter = counter + 1
                    if min(
                            radius) < 1.3:  # filter out every function with a radius of curvature smaller            ### OBS! Check this value
                        break  # than that of renault twizy



                    for x in lengtharray:
                        if x != 0:
                            f_deriv = f_arctan_d1(a, b, c, x)  # first derivative
                            collision = filter_collision(x, f_arctan(a, b, c, x), f_deriv)

                            if collision == True:
                                collision1 = True

                    if collision1 == True:
                        break

                    plt.plot(lengtharray, function)

                    #return  [a, b, c]

                    # TODO: Returnera a,b,c på bästa funktionen!
                    # TODO: IF NO PATH IS CALCULATED, LOWER THE FIRST 2 CRITERIAS
                    # TODO: FIND BEST VALUES FOR PHASE AND DEPTH.ETC
                    # TODO: MAKE THE CODE COMPATIBLE WITH A DYNMAIC MAP

offset = 2
parkingLength = 5.5
distance = 1
current = Coordinate(0, 0)
goal = Coordinate(5, distance + 1.25)
lst = np.linspace(offset, parkingLength + offset)
print(Convert(lst))


karta = makeMap()
plt.plot(list(karta.keys()), list(karta.values()), 'black')
# plt.show()

path(current, goal)
plt.show()


