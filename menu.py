## Text menu in Python
## Pahor.m @Oktober 2022
## python via termux in nano editor
def print_menu(): ## Your menu design here
        print ("_"*5 , "MENU" , "-"*5)
        print ("1. Menu Option 1")
        print ("2. Menu Option 2")
        print ("3. Menu Option 3")
        print ("4. Menu Option 4")
        print ("5. Exit")
        print (16 * "-")

def chek_num():
        while True:
          try:
             return int(input("Enter your choice [1-5]:" ))
             break;
          except ValueError:
             print ("Invalid input")
#--------------+++++
loop = True
while loop:
## While loop which will keep going until loop = False
  print_menu()
## Displays menu
  #choice = int(input("Enter your choice [1-5]: "))
  choice = chek_num()
  if choice == 1:
    print ("Menu 1 has been selected")
## You can add your code or functions here
  elif choice==2:
    print ("Menu 2 has been selected")
## You can add your code or functions here
  elif choice==3:
    print ("Menu 3 has been selected")
## You can add your code or functions here
  elif choice==4:
    print ("Menu 4 has been selected")
## You can add your code or functions here
  elif choice==5:
    print ("Menu 5 has been selected")
## You can add your code or functions here
    loop=False # This will make the while loop to end as not value of loop is set to False
  else:
# Any integer inputsto other than values 1-5 we print an error message
    print ("Enter your choice to try again..")
