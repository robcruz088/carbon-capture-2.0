import serial
import random
import string
import datetime
import json


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


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Generate ID's for the database. Can increase the size but works best when the character
    parameter is kept to its default value. Uses a random choice from the characters given to generate
    the ID.
    :param size: size of the IDs, defaults to 6. Max size: 36
    :param chars: characters for the ID. defaults to uppercase letter and  number number combination
    :return: string ID
    """
    return ''.join(random.choice(chars) for _ in range(size))

def toJson(jsonFileName: str, dataPayload: list):
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
        "Particulate Matter(PM1/PM2.5/PM10)": [
            dataPayload[3],
            dataPayload[4],
            dataPayload[5]
        ],
        "_id": id_generator()
    }

    with open(jsonFileName, 'w') as jsonFile:
        json.dump(sensorData, jsonFile)

def readFromJson(jsonFileName, ):
    """
    Simple function to read the JSON
    :param jsonFileName: the JSON file name
    :return:
    """
    with open(jsonFileName, 'r') as jsonFile:
        sensorData = json.load(jsonFile)
    print(sensorData)
    return sensorData


#               _
#  quack      >(.)__
#              (___/