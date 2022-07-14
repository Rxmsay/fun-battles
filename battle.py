import random
import time
import colorama
from colorama import Fore, Back, Style  #you have to install colorama

random.choice(range(1, 25))
n1 = input(Fore.CYAN + "enter name1: ")
n2 = input(Fore.RED + "enter name2: ")

i1 = 100
i2 = 100

while i1 < 101:
    print(f"{Fore.CYAN} {n1}'s health is: {Style.RESET_ALL} {i1}")
    i1 = i1 - random.choice(range(-2, 35))
    time.sleep(0.6)

    print(Style.RESET_ALL + "---------------------------")
   

    print(f"{Fore.RED} {n2}'s health is: {Style.RESET_ALL} {i2}")
    i2 = i2 - random.choice(range(-2, 35))
    time.sleep(0.6)

    print(Style.RESET_ALL + "---------------------------")




    if i1 <= 0 and i1 < i2:
        print(f"{Fore.CYAN} {n1}'s health is: 0 DEAD")
        break
        
    
    elif i2 <= 0 and i2 < i1:
        print(f"{Fore.RED} {n2}'s health is: 0 DEAD")
        break
        
              
            
        


