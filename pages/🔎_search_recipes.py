import streamlit as st
from urllib.parse import quote_plus
from pymongo import MongoClient

username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['recipe-book']
collection = db['recipes']


#Header
st.title("All your recipes")


# Sidebar
st.sidebar.header("Search Filters")
difficulty = st.sidebar.selectbox("Difficulty", ['Any', 'Easy', 'Medium', 'Hard'])
cook_time = st.sidebar.slider("Maximum Cooking Time (minutes)", 0, 120, 60)

search_query = st.text_input("Search for recipe by name or ingredient")

#search button
if st.button("Search"):
   query = {}
   if search_query:   #checking if the search query has information/what the user uploaded
       query['$or'] = [            #If contains x , i want to fetch x
           {"name": {"$regex": search_query, "$options": "i"}}, #Adding the diff fields, I want to mke the query filter. Name is the key and the value is whatever info is in my search query.
           {"ingredients": {"$regex": search_query, "$options": "i"}}
       ]
       st.write(f"Searching for recipes with: {search_query}")

    
   else:
      st.error("Please enter a search query")

   recipes = list(collection.find(query, {"_id": 0, "name": 1, "image": 1, "ingredients": 1, "instructions": 1, "cook_time": 1, "difficulty": 1}))
   if recipes: #checking if recipe list has info
       for recipe in recipes:
           st.write(recipe['name'])
           st.write(recipe['ingredients'])
      
      
      
   


#footer
st.markdown("---")   
st.markdown("Made using Streamlit")      

# the regex function from mongodb is being used to bring the info that we have from the search query(basically the txt the user wrote)
# theoptions finction is to display any info that is present in the database