import serial

arduinoData = serial.Serial('COM3', 9600)
#arduinoData = serial.Serial('/dev/ttyACM0', 9600) # for rpi

while True:
    if arduinoData.in_waiting > 0:
        pass
    arduinoString = str(arduinoData.readline(),'utf-8')
    dataArray = [x.strip() for x in arduinoString.split(',')]
    print(dataArray)