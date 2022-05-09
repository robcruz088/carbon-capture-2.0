from payloadData import payload, id_generator
from databaseAuth import connectDatabase


username = input("Enter Database Username: ")
password = input("Enter Database Password: ")
databaseName = input("Enter Database Name: ")

client = connectDatabase(username,password,databaseName)

try:
    db = client['sensor_data'] # database in the mongoDB cluster
    db_collection = db['sensor'] # collection in the data base

## TODO: CREATE PROPER JSON FILE
    sensor_data = {"Temperature(C/F)": ["", ""],
                   "Humidity(%)": "",
                   "_id": ""
                   }

    while True:
        arduinoConnection = payload('COM3', 9600)
        sensor_data["Temperature(C/F)"][0] = arduinoConnection[0]
        sensor_data["Temperature(C/F)"][1] = arduinoConnection[1]
        sensor_data["Humidity(%)"] = arduinoConnection[2]
        sensor_data["_id"] = id_generator()

        db_collection.insert_one(sensor_data)  # insert a new document each iteration

        #print("Celsius: %s | Fahrenheit: %s | Humidity: %s" % (arduinoConnection[0], arduinoConnection[1], arduinoConnection[2]))

except TypeError:
    print("Connection Failed. Goodbye!")


