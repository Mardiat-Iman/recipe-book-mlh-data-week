import streamlit as st

st.title("Add a new dish!!")

recipe_name = st.text_input("Recipe Name") #text input is one line
ingredients = st.text_area("Ingredients") #text area takes up much more spcae so can be used for largechunks of text
instructions = st.text_area("Instructions")
cook_time = st.number_input("Cooking Time", step=1) #hve to specify what our no input will be receiving.
difficulty = st.selectbox("Difficulty", ['Easy', 'Medium', 'Hard']) #Allows user select from diff options
image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg']) #Allow user to upload a file  

if st.button("Send recipe"): #creates a button and checks if its clicked
    if recipe_name and ingredients and instructions:                                
        st.success("Recipe was sent correctly")
    else:
        st.error("Please fill the missing fields")  