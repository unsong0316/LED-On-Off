

import time
value = [aa for aa in range(3)]

for num in range (24,27):
        direction = open("/gpio/pin"+str(num)+"/direction","w")
        direction.writelines("out")

def redon():
    value[0] = open("/gpio/pin24/value","w")
    value[0].writelines("1")
    value[0].close()
    
def greenon():
     value[1] = open("/gpio/pin25/value","w")
     value[1].writelines("1")
     value[1].close()

def blueon():
    value[2] = open("/gpio/pin26/value","w")
    value[2].writelines("1")
    value[2].close()

def redoff():
    value[0] = open("/gpio/pin24/value","w")
    value[0].writelines("0")
    value[0].close()
    
def greenoff():
    value[1] = open("/gpio/pin25/value","w")
    value[1].writelines("0")
    value[1].close()

def blueoff():
    value[2] = open("/gpio/pin26/value","w")
    value[2].writelines("0")
    value[2].close()
    
while(1):

    redon()
    time.sleep(1)
    redoff()
    time.sleep(1)
    greenon()
    time.sleep(1)
    greenoff()
    time.sleep(1)
    blueon()
    time.sleep(1)
    blueoff()
    time.sleep(1)
    redon()
    greenon()
    time.sleep(1)
    redoff()
    greenoff()
    time.sleep(1)
    greenon()
    blueon()
    time.sleep(1)
    greenoff()
    blueoff()
    time.sleep(1)
    redon()
    greenon()
    blueon()
    time.sleep(1)
    redoff()
    greenoff()
    blueoff()
    time.sleep(1)
    
