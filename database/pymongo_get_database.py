from dotenv import load_dotenv
from pymongo import MongoClient
import os
import requests
load_dotenv()


def get_database():
    conn_str = os.getenv('CONNECTION_STRING')
    client = MongoClient(conn_str)
    return client['LineUP-Predictor']
