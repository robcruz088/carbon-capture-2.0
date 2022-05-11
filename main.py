from payloadData import payload, toJson, readFromJson
from databaseAuth import connectDatabase


# credentials to connect to the database
username = input("Enter Database Username: ")
password = input("Enter Database Password: ")
databaseName = input("Enter Database Name: ")

client = connectDatabase(username,password,databaseName)

try:
    db = client['sensor_data'] # database in the mongoDB cluster
    db_collection = db['sensor'] # collection in the data base

    while True:
        arduinoConnection = payload('COM3', 9600)

        # the purpose of this is only to make the code look cleaner
        # can be done without a JSON file for this specific case

        toJson("payload_data.json",arduinoConnection) # send data to JSON
        jsonPayload = readFromJson("payload_data.json") # read JSON file (dict object)

        # to database
        db_collection.insert_one(jsonPayload)  # insert a new document each iteration



except TypeError:
    # error handler
    print("Connection Failed. Goodbye!")

#               _
#  quack      >(.)__
#              (___/  