from pymongo import MongoClient
import pymongo.errors

def connectDatabase(user,password, dabatase_name):
    """
    authentication for connecting to the MongoDB Database
    :param user: username of database access
    :param password: database access user password
    :param dabatase_name: name of the database to connect to
    :return:
    """

    try:
        client = MongoClient(
                "mongodb+srv://%s:%s@testcluster.dzoyl.mongodb.net/%s?retryWrites=true&w=majority" %
                (user, password, dabatase_name) )
        client.server_info() # check for connection
        print("Authentication Successful!")
        return client

    except pymongo.errors.OperationFailure:
        print("Could not connect to the database!")








