# cara menggunakan math.tan2
# Pahor.m @Oktober 2022
# python via termux
import math
print ('#BasePoint#')
# input East7
while True:
    try:
        BaseEast = float(input("East : "))
        print ("You entered: ",BaseEast)
        break;
    except ValueError:
        print ("Invalid input")

# input North
while True:
    try:
        BaseNorth = float(input("North : "))
        print ("You entered: ",BaseNorth)
        break;
    except ValueError:
        print ("Invalid input")

print ('East ' + str(BaseEast) + ',' + 'North ' + str(BaseNorth))
#≠==========÷========================
print ('#TargetPoint#')
# input East
while True:
    try:
        TargetEast = float(input("East : "))
        print ("You entered: ",TargetEast)
        break;
    except ValueError:
        print ("Invalid input")

# input North
while True:
    try:
        TargetNorth = float(input("North : "))
        print ("You entered: ",TargetNorth)
        break;
    except ValueError:
        print ("Invalid input")

print ('East ' + str(TargetEast) + ',' + 'North ' + str(TargetNorth))

nLat = TargetEast-BaseEast
nDef = TargetNorth - BaseNorth
Azimut = math.atan2 (nLat,nDef)
print ("Azimut Rad " + str(Azimut))
print ("Azimut Deg " + str(math.degrees(Azimut)))

