import mysql.connector
from dotenv import load_dotenv
from os import getenv
load_dotenv()


def connection():
    connect = mysql.connector.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('PASSWORD'),
                                      database=getenv('DB'))
    return connect


def suma(a, b):
    return a + b
