# Perhitungan Waterpass/Autolevel
# Pahor.m @Oktober 2022
# python via termux
import math

from prettytable import PrettyTable
TabBS = PrettyTable()
TabBS.title = "BS"
TabBS.field_names = ["BT", "BA", "BB"]
fBS = False


TabFS = PrettyTable()
TabFS.title = "FS"
TabFS.field_names = ["BT", "BA", "BB"]

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

def input_BS():
# Variable BS
  print (bcolors.BOLD,'#BackSight#',bcolors.ENDC)

# input BS
  while True:
    try:
        BS_BT = float(input("BT : "))
        break;
    except ValueError:
        print ("Invalid input")

  while True:
    try:
        BS_BA = float(input("BA : "))
        break;
    except ValueError:
        print ("Invalid input")

  while True:
    try:
        BS_BB = float(input("BB : "))
        break;
    except ValueError:
        print ("Invalid input")

  TabBS.add_row([BS_BT,BS_BA,BS_BB])
#≠==========÷=========================
def input_FS():
  print (bcolors.BOLD,'#FrontSight#',bcolors.ENDC)
# input FS
  while True:
    try:
        FS_BT = float(input("BT : "))
        break;
    except ValueError:
        print ("Invalid input")

  while True:
    try:
        FS_BA = float(input("BA : "))
        break;
    except ValueError:
        print ("Invalid input")

  while True:
    try:
        FS_BB = float(input("BB : "))
        break;
    except ValueError:
        print ("Invalid input")

0  TabFS.add_row([FS_BT,FS_BA,FS_BB])

#≠========================≠===================
input_BS()
input_FS()

yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

while True:
  user_input = input('FrontSight Again (yes/no): ')
  if user_input.lower() in yes_choices:
       input_FS()
       continue
  elif user_input.lower() in no_choices:
       print ('exit...!')
       break
  else:
       print ('Type yes or no')
       continue


#start   =  1
#limit   =  len(FS_LST)

#idxstr  =  0
#idxmax  =  limit - 1

#print (start,"|",BS_LST[0],"|",NULL_LST)
#start=start+1

#while(idxstr<=idxmax):
#  TabFS.add_row(FS_LST)
#  start=start+1
#  idxstr=idxstr+1

print (TabBS)
print (TabFS)

print (bcolors.OKYELLOW,'Pahor.m @Oktober 2022',bcolors.ENDC)
print (bcolors.OKYELLOW,'Foreman Surveyor',bcolors.ENDC)

