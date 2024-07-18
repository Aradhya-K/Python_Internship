import math
def circum(length):
    return 2*math.pi*length

dia=int(input("enter the diameter:"))

rad=dia/2
res=circum(rad)

print('the circumference of the circle with radius {} is {}'.format(rad,res))