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


st.title("Add a new dish!!")

recipe_name = st.text_input("Recipe Name") #text input is one line
ingredients = st.text_area("Ingredients") #text area takes up much more spcae so can be used for largechunks of text
instructions = st.text_area("Instructions")
cook_time = st.number_input("Cooking Time", step=1) #hve to specify what our no input will be receiving.
difficulty = st.selectbox("Difficulty", ['Easy', 'Medium', 'Hard']) #Allows user select from diff options
image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg']) #Allow user to upload a file  

if st.button("Send recipe"): #creates a button and checks if its clicked
    if recipe_name and ingredients and instructions and cook_time and difficulty:   
        image_data = image.read()   if image else None

        recipe = {          # this is basically what the user will input and the info goes into the mongo cluster
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "cook_time": cook_time,
            "difficulty": difficulty,
            "image": image_data
        }  

        collection.insert_one(recipe)     #basically inserting the above document                    
        st.success("Recipe was sent correctly")
    else:
        st.error("Please fill the missing fields")  



#footer
st.markdown("---")   
st.markdown("Made using Streamlit")      