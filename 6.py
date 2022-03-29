import math
r=int(input("반지름 내놔"))

T= 4*math.pi*r*r
SS=(4/3)*math.pi*(r*r*r)
print("겉면적은 ={}".format(T))
print("부피는 ={}".format(SS))

#6