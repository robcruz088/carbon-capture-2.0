from pymongo import MongoClient
import pymongo.errors

def connectDatabase(user,password, dbName):
    """
    authentication for connecting to the MongoDB Database
    :param user: username of database access
    :param password: database access user password
    :param dbName: name of the database to connect to
    :return:
    """

    try:
        client = MongoClient(
                "mongodb+srv://%s:%s@%s.dzoyl.mongodb.net/%s?retryWrites=true&w=majority" %
                (user, password, dbName, dbName) )
        client.server_info() # check for connection
        print("Authentication Successful!")
        return client

    except pymongo.errors.OperationFailure:
        print("Could not connect to the database!")








