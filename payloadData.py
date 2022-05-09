import serial
import random
import string


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
