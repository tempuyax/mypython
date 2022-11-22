
from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

#print (x.get_string(sortby="Population"))
#x.sortby = None


#-----------------+++++
def print_menu(): ## Your menu design here
        print ("_"*5 , "MENU" , "-"*5)
        print ("1. View Default")
        print ("2. View Selected fields")
        print ("3. View Range 1-4")
        print ("4. View Aligned")
        print ("5. Exit")
        print (16 * "-")

def chek_num():
        while True:
          try:
             return int(input("Enter your choice : "))
             break;
          except ValueError:
             print ("Invalid input")
#--------------+++++
loop = True
while loop:
## While loop which will keep going until loop = >
  print_menu()
## Displays menu
  choice = chek_num()
  if choice == 1:
    print (x)
  elif choice==2:
    print (x.get_string(fields=["City name", "Population"]))
  elif choice==3:
    print (x.get_string(start=1, end=4))
  elif choice==4:
    x.align["City name"] = "l"
    x.align["Area"] = "c"
    x.align["Population"] = "r"
    x.align["Annual Rainfall"] = "c"
    print (x)
    print ("Menu 4 has been selected")
  elif choice==5:
    loop=False # Exit
    # This will make the while loop to>
  else:
    # Any integer inputsto other than values 1-5 we p>
    print ("Enter your choice to try again..")



