import os

while True :
    commend = input("what do you do : \n 1 : create a fil \t \t 2 : create a new directory \n 3 : open a old fil \t \t 4 : Write a special commend \n =>>>> : ").strip()
    
    if commend == "1" :
        path = input("wher is  a place of the fil : ")
        name_of_fil = input("name of fil : ")
        fil = open(f"{path}/{name_of_fil}","a")
    
    elif commend == "2": 
        dire = input('entre a dir : ')
        os.system(f"mkdir {dire}")
    
    elif commend == "3":
        fil = input("entre a file to open : ")
        prog_to_open = input("open with : ")
        os.system(f"{prog_to_open} {fil}")
    
    elif commend == "4": 
        com = input("Entre your commend : ")
        os.system(f"{com}")