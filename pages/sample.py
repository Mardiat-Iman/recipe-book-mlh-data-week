import streamlit as st
from urllib.parse import quote_plus
from pymongo import MongoClient

username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['sample-recipe']
collection = db['recipes-2']

st.write('Experimenting if users can have a chatbot using vector database and semantics searching')