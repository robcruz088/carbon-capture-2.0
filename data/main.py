from payloadData import payload, dataCollection
from databaseAuth import connectDatabase


# credentials to connect to the database
username = input("Enter Database Username: ")
password = input("Enter Database Password: ")
databaseName = input("Enter Database Name: ")

client = connectDatabase(username,password,databaseName)

try:
    dataBase = client['sensor_data'] # database in the mongoDB cluster
    databaseCollection = dataBase['sensor'] # collection in the data base

    while True:
        arduinoConnection = payload('COM3', 115200)

        sensorData = dataCollection(arduinoConnection)

        # to database
        databaseCollection.insert_one(sensorData)  # insert a new document each iteration



except TypeError:
    # error handler
    print("Connection Failed. Goodbye!")

#               _
#  quack      >(.)__
#              (___/