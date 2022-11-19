import smbus              # Library used for I2C communication
import time               # Time library used for adding delay function

# Here we have set the address for the sensor
LIGHT_SENSOR = 0X23       

VALUE = 0X23

bus=smbus.SMBus(1)     # Here we have set the I2C port to 1 

# Here we have defined the function "reading", the data from the sensor is processed using this 

def reading():
    data = bus.read_i2c_block_data(LIGHT_SENSOR,VALUE)
    return ((data[1] + (256*data[0]))/1.2)                # Converting the reading into decimal format

# Here we have made a loop that will print the messages and the readings from the sensor according to the parametes

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
