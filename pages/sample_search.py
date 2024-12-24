import streamlit as st
from urllib.parse import quote_plus
from pymongo import MongoClient
from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from num2words import num2words

username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['sample-recipe']
collection = db['recipes-2']

#Create embeddings by stating model and tokenizer which are from BERT hugging face
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') #the bert model being used
model = BertModel.from_pretrained('bert-base-uncased')

#converting numbers to words
def convert_numbers_to_words(text):
    words = text.split()  # Split text into words
    for i, word in enumerate(words):
        if word.isdigit():  # Check if the word is a number
            words[i] = num2words(int(word))  # Convert the number to words
    return ' '.join(words)  # Rejoin words back into a string

#to convert text responses into embeddings
def generate_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True) #responses to the form, pt is pytorch
    output = model(**inputs)
    embedding = output.last_hidden_state.mean(dim=1).detach().numpy() #converting from tensorarray to numpy
    return embedding

st.title("Add a new dish!!")

recipe_name = st.text_input("Recipe Name") #text input is one line
ingredients = st.text_area("Ingredients") #text area takes up much more spcae so can be used for largechunks of text
instructions = st.text_area("Instructions")
difficulty = st.selectbox("Difficulty", ['Easy', 'Medium', 'Hard']) #Allows user select from diff options
cook_time = st.number_input("Cooking Time", step=1) #hve to specify what our no input will be receiving.
image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg']) #Allow user to upload a file  


if st.button("Send recipe"): #creates a button and checks if its clicked
    if recipe_name and ingredients and instructions  and difficulty:   
        cook_time_in_words = convert_numbers_to_words(str(cook_time))  # Convert the cooking time to words
       

        recipe2 = {          # this is basically what the user will input and the info goes into the mongo cluster
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "difficulty": difficulty,
            "cook_time": cook_time,
            #"image": image   Don't want to encode the images
    
        }  

       
        concatenated_responses = f"{recipe_name} {ingredients} {instructions} {difficulty} {cook_time_in_words}"                 
        embeddings = generate_embeddings(concatenated_responses)
        st.write(embeddings)
        
        document = {
            "recipe2": recipe2,
            "embeddings":embeddings.tolist()
        }
        #client["sample-recipe"]["recipe2"].insert_one(document)
        collection.insert_one(document)

        #cosine similarity
        all_documents = list(collection.find())
        if all_documents:
            #A recipe inputted by user is a current embedding (vector1)
            current_embedding = embeddings.flatten() # .flatten converts to 1D
            #Store similar recipes from the database
            similarities = []

            for doc in all_documents: #iterating over all the elements in the document
                store_embedding = np.array(doc["embeddings"]).flatten()
                similarity = np.dot(current_embedding, store_embedding) / (np.linalg.norm(current_embedding)) * np.linalg.norm(store_embedding)
                similarities.append((doc, similarity))


                similarities = sorted(similarities, key=lambda x:x[1], reverse=True)

                #Print for our top 3 matches
                #st.write(similarities)
                st.subheader("Your top 2 matches")
                st.divider()
                for match, similarity in similarities[:2]:
                    st.write(similarity)
                    st.write(match["recipe2"])



        st.success("Recipe was added correctly")
    else:
        st.error("Please fill the missing fields")  



#footer
st.markdown("---")   
st.markdown("Made using Streamlit")      