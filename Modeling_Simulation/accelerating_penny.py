#####################################################
#
#           Calculate for Velocity 
#                   v = at
#
#####################################################

a = 9.81
t = int(input("Enter the time in seconds: "))

v = a * t

print("The velocity of the penny is: ", v, "m/s")

##############################################################
#
#           Calculate for Distance *ignoring air resistance*
#                          x = at² / 2
#
##############################################################

x = a * t**2 / 2

print("The distance the penny has dropped is: ", x, "m")

##############################################################
#
#                      Calculate for time 
#                        t = √(2x / a)
#
##############################################################

from numpy import sqrt

h = int(input('What is the height in meters that the object is falling from? : '))

t = sqrt(2 * h / a)
v = a * t
print('The time it took to fall ', h, 'meters was ', t, 'seconds at ', a, 'm/s.')