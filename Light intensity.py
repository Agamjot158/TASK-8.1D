import smbus
import time

LIGHT_SENSOR = 0X23

VALUE = 0X23

bus=smbus.SMBus(1)

def reading():
    data = bus.read_i2c_block_data(LIGHT_SENSOR,VALUE)
    return ((data[1] + (256*data[0]))/1.2)


while True:
    light=reading()
    print("Light intensity is: " + str(light))
   
    if(light>=1000):
        print("Too Bright")
    elif(500<light<1000):
        print("Bright")
    elif(100<light<500):
        print("Medium")
    elif(50<light<100):
        print("Dark")
    elif(light < 50):
        print("Too Dark")
    
    time.sleep(1)
