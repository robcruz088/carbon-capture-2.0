import serial
import random
import string
import datetime
import time


def payload(com: str, baudRate = 9600):
    """
    :param com: the port for serial connection
    :param baudRate: rate of info transferred. Defaults to 9600 but
           can be changed to whatever value is needed from the Arduino
    :return: data array containing the arduino payload
    """

    arduinoData = serial.Serial(com, baudRate)
    while True:
        if arduinoData.in_waiting > 0:
            pass

        # decode up the payload data- from b'string to a regular string
        arduinoString = str(arduinoData.readline(),'utf-8')

        # put the values in an array
        dataArray = [x.strip() for x in arduinoString.split(',')]

        return dataArray


def idGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Generate ID's for the database. Can increase the size but works best when the character
    parameter is kept to its default value. Uses a random choice from the characters given to generate
    the ID.
    :param size: size of the IDs, defaults to 6. Max size: 36
    :param chars: characters for the ID. defaults to uppercase letter and  number number combination
    :return: string ID
    """
    return ''.join(random.choice(chars) for _ in range(size))

def getTime():
    """
    Get the current time in UTC
    :return: datetime object in UTC
    """
    utcTime = datetime.datetime.utcnow()

    return utcTime

def dataCollection(dataPayload: list):
    """
    Simple function to write to a JSON file
    :param jsonFileName: JSON filename
    :param dataPayload: takes a list in order to put it in a JSON
    """

    # dictionary. Will be updated eventually to be more
    # scalable for different types of JSON with list
    sensorData = {
        "Temperature(C/F)": [
            dataPayload[0],
            dataPayload[1]
        ],
        "Humidity(%)": dataPayload[2],
        "PM(S/M/D)": [
            dataPayload[3],
            dataPayload[4],
            dataPayload[5]
        ],
        "CO(PPM)":dataPayload[6],
        "_id": idGenerator(),
        "Timestamp": getTime()
    }

    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S",t) # for debug purposes
    print(sensorData,"\n",currentTime)
    return sensorData


#               _
#  quack      >(.)__
#              (___/