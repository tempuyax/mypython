# cara menggunakan math.atan2
# Pahor.m @Oktober 2022
# python via termux
import math

# Coloring text mode
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[33m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function Angle 360 Controling
def sign_360(Azimut):
    if Azimut > 0:
        return Azimut       # 1 or Positive Angle
    elif Azimut == 0:
        return 0.0          # 0 or Zero Angle
    else:
        return Azimut + 360 # -1 or Negative Angle

print (bcolors.BOLD,'#BasePoint#',bcolors.ENDC)
# input East
while True:
    try:
        BaseEast = float(input("East : "))
        #print ("You entered: ",BaseEast)
        break;
    except ValueError:
        print ("Invalid input")

# input North
while True:
    try:
        BaseNorth = float(input("North : "))
        #print ("You entered: ",BaseNorth)
        break;
    except ValueError:
        print ("Invalid input")

#print ('East ' + str(BaseEast) + ',' + 'North ' + str(BaseNorth))

#≠==========÷=========================
print (bcolors.BOLD,'#TargetPoint#',bcolors.ENDC)

# input East
while True:
    try:
        TargetEast = float(input("East : "))
 #       print ("You entered: ",TargetEast)
        break;
    except ValueError:
        print ("Invalid input")

# input North
while True:
    try:
        TargetNorth = float(input("North : "))
#        print ("You entered: ",TargetNorth)
        break;
    except ValueError:
        print ("Invalid input")

#print ('East ' + str(TargetEast) + ',' + 'North ' + str(TargetNorth))

# Main Calculation of Bearing
nLat = TargetEast-BaseEast
nDef = TargetNorth - BaseNorth
AzimutRad = math.atan2 (nLat,nDef)
AzimutDeg = math.degrees(AzimutRad)
Azimut360 = sign_360(AzimutDeg)
print (bcolors.BOLD,'~Bearing~',bcolors.ENDC)
print ("Azimut (Rad) " + str(AzimutRad))
print ("Azimut (Deg) " + str(AzimutDeg))
print ("Azimut (360) " + str(Azimut360))

# DMS Angle Format
D = int(Azimut360)
M = int((Azimut360-D)*60)
S = int((((Azimut360-D)*60)-M)*60)

HD = math.dist([TargetEast,TargetNorth],[BaseEast,BaseNorth])

print (bcolors.OKCYAN,'Geodetic Instrument',bcolors.ENDC)
print ("HA :", str(D),"°",str(M),'"',str(S),"'")
print ("HD :", str(HD))

#print (repr(f'{HD:8.3f}'))

print (bcolors.OKYELLOW,'Pahor.m @Oktober 2022',bcolors.ENDC)
print (bcolors.OKYELLOW,'Foreman Surveyor',bcolors.ENDC)

