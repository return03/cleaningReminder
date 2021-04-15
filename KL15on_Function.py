from concurrent import futures
from time import sleep
import datetime


def startUpScreen():
    userInput=""
    print("Hello and welcome, what do you want to do? (Press 's' if you want to start the function, press 'e' if you want to stop the engine")
    while(userInput!="e"):
        userInput=input()
        if userInput=="s":
            if cycleFlag==0:
                startFsunc()
            else:
                print("You can`t use this function twice in one cycle")
    if userInput=="e":
        print("I hope you enjoyed your trip")
        quit()
        
    else:
        print("This input is not possible")

def startCar():
    while(1):
        print("...")
        sleep(1)


def startFunc():
    global cycleFlag 
    cycleFlag=1
    verb=" started "
    for i in range(0,2,1):
        now = datetime.datetime.now()
        print("Function", verb, " at: ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        verb=" ended "
        sleep(5)


cycleFlag=0
if __name__== "__main__":
    with futures.ThreadPoolExecutor(max_workers=3) as cord:
        cord.submit(startUpScreen)
        cord.submit(startCar)


        
