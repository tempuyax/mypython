# Menghitung data ukur theodolit
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
        bN = float(input("N: "))
        #print ("You entered: ",BaseEast)
        break;
    except ValueError:
        print ("Invalid input")

# input North
while True:
    try:
        bE = float(input("E: "))
        #print ("You entered: ",BaseNorth)
        break;
    except ValueError:
        print ("Invalid input")

# input Zenith
while True:
    try:
        bZ = float(input("Z: "))
        #print ("You entered: ",BaseNorth)
        break;
    except ValueError:
        print ("Invalid input")

#print ('East ' + str(BaseEast) + ',' + 'North ' + str(BaseNorth))

#≠==========÷=========================
print (bcolors.BOLD,'#Instrument Theodolit#',bcolors.ENDC)

# input East
while True:
    try:
        HI = float(input("HI: "))
        # print ("You entered: ",TargetEast)
        break;
    except ValueError:
        print ("Invalid input")

# input East
while True:
    try:
        BT = float(input("BT: "))
        # print ("You entered: ",TargetEast)
        break;
    except ValueError:
        print ("Invalid input")

# input North
while True:
    try:
        BA = float(input("BA: "))
#        print ("You entered: ",TargetNorth)
        break;
    except ValueError:
        print ("Invalid input")


#def Release():

 #
 #   try:
 #       print 'Please select one of the following?\nCompletion = 0\nRelease ID = 1\nVersion ID = 2\Build ID = 3
 #       a = int(input("Please select the type of release required: "))
 #       if a == 0:
 #           files(a)
 #       elif a == 1:
 #           files(a)
 #       elif a == 2:
 #           files(a)
 #       elif a == 3:
 #           files(a)
 #       else:
 #           raise 'incorrect'
 #   except 'incorrect':
 #       print 'Try Again'
 #   except:
 #       print 'Error'

#Release()

while True:
    try:
        VA = float(input("VA (DD.MMSS): "))
        #print (VA)

        Dd = int(VA)
        if Dd < 180:
           VA = ((VA-Dd)*100)
        else:
           print ("Degree Max 180")
           raise  ValueError

        Md = int(VA)
        if Md < 60:
           VA = ((VA-Md)*100)
        else:
           print ("Minute Max 60")
           raise ValueError

        Sd = round(VA)
        if Sd < 60:
           VA = Dd+(Md/60)+(Sd/3600)
        else:
           print ("Secone Max 60")
           raise ValueError

        break;
    except ValueError:
        print ("Invalid input")

while True:
    try:
        HA = float(input("HA (DD.MMSS): "))
        #print (HA)
        Dd = int(HA)
        HA = ((HA-Dd)*100)
        #print (HA)
        Md = int(HA)
        HA = ((HA-Md)*100)
        #print (HA)
        Sd = round(HA)
        #print ("You entered: ",Dd," ",Md," ",Sd)
        #print ("Decimal HA : ",Dd+(Md/60)+(Sd/3600))
        HA = Dd+(Md/60)+(Sd/3600)
        break;
    except ValueError:
        print ("Invalid input")


#print ('East ' + str(TargetEast) + ',' + 'North ' + str(TargetNorth))

# Main Calculation of Polar coordinat
SD = (BA-BT)*200
HD = math.sin(math.radians(VA))*SD

dN = (SD * math.sin(math.radians(VA))) * math.cos(math.radians(HA))
dE = (SD * math.sin(math.radians(VA))) * math.sin(math.radians(HA))
dZ = (SD * math.cos(math.radians(VA))) + HI - BT

N = bN + dN
E = bE + dE
Z = bZ + dZ

print (bcolors.BOLD,'#Distance Point#',bcolors.ENDC)
print ("SD: ",round(SD,3))
print ("HD: ",round(HD,3))

print (bcolors.BOLD,'#Delta Point#',bcolors.ENDC)
print ("dN:",round(dN,3))
print ("dE:",round(dE,3))
print ("dZ:",round(dZ,3))

print (bcolors.BOLD,'#Target Point#',bcolors.ENDC)
print ("N:",round(N,3))
print ("E:",round(E,3))
print ("Z:",round(Z,3))

