import time #import time to allow a time delay
print("***************************************")
print("welcome to the greateset drinks machine")#welcoming user
print("***************************************")
time.sleep(2)
drink=int(input("press 1 for tea or press 2 for coffee"))
if drink == 1:          #user iks selecting their drink
    time.sleep(1)
    print("you have selected tea")          
elif drink == 2:
    time.sleep(1)
    print("you have selected coffee")
else:
    print("an unexcpected error has occured pleas try again")
    quit()
time.sleep(1)    
sugar=int(input("please enter the amount of sugar you would like"))
if sugar >0:    #user is selecting the amount of sugar they would like
    time.sleep(1)
    print("you have selected",sugar,"sugars")
else:
    time.sleep(1)
    print("you have selected no sugar")
time.sleep(1)    
milk=int(input("please enter 1 if you would like your drink strong,2 for medium and 3 for weak"))
if milk==1:   #user is choosing the amount of milk they would like
    time.sleep(1)
    print("you have selected your drink to be strong")
elif milk==2:
    time.sleep(1)
    print("you have selected your drink to be medium")
elif milk==3:
    time.sleep(1)
    print("you have selected your drink to be weak")
else:
    print("unexcpected error has occured please try again")
    quit()
time.sleep(1)    
cup=int(input("please enter 1 for a small drink,2 for medium and 3 for large"))
if cup ==1: #user is choosing cup size
    time.sleep(1)
    print("you have selected a small drink")
elif cup ==2:
    time.sleep(1)
    print("you have selected a medium drink")
elif cup ==3:
    time.sleep(1)
    print("you have selected a large drink")
else:          
    print("unexpected error please try again")
    quit()
    time.sleep(1) 
input("press enter to start pouring drink")  
print("pouring....") #drink is pouring
time.sleep(2)#time delay by 2 seconds
print("your drink has been poured")
print("enjoy!")  #drink is poured


    


