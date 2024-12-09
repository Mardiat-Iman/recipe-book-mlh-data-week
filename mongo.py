#pings our database to make sure we are ready to get info from there
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
from urllib.parse import quote_plus #This allows you to basically escape the secrets credential. 

username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]
#f is to format the text
uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)