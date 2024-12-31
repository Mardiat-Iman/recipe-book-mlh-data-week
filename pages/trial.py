import streamlit as st
from urllib.parse import quote_plus
from pymongo import MongoClient
import base64

username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['recipe-book']
collection = db['recipes']

recipes = list(collection.find({}, {"name": 1, "image": 1}))


# Function to get base64 encoding for images

def get_image_base64(binary_image):
    # Check if the image is None
    if binary_image is None:
        return None  # may make putting an image compulsory so the format comes out nice or put a default image
    
    # Proceed with encoding if the image is valid
    return base64.b64encode(binary_image).decode('utf-8')

# Fetch recipes from MongoDB
recipes = list(collection.find())

def display_recipe_grid(recipes):
    for i in range(0, len(recipes), 2):
        cols = st.columns(2)
        for col, recipe in zip(cols, recipes[i:i+2]):
            with col:
                # Base64 encoding for the image
                image_base64 = get_image_base64(recipe["image"])  # Assuming 'image' field stores path
                
                # Display the recipe as a clickable button (with image and name)
                button_id = f"select_{recipe['_id']}"  # Unique ID for each button
                if st.button(f"{recipe['name']}", key=button_id):
                    # If clicked, store the recipe's ID in session state
                    st.session_state.selected_recipe_id = str(recipe["_id"])
                    st.rerun()

                # Display the recipe image (just for visual appeal)
                st.image(f"data:image/jpg;base64,{image_base64}", use_container_width=True)

# Function to handle ingredients display
def display_ingredients(ingredients):
    # Split the ingredients string by line breaks ('\n') to handle each ingredient separately
    ingredients_list = ingredients.split("\n")
    
    # Display ingredients as a comma-separated string
    st.write(f"**Ingredients:** {', '.join(ingredients_list)}")

    # Alternatively, if you want to display them as a bulleted list:
    # st.write("**Ingredients:**")
    # for ingredient in ingredients_list:
    #     st.write(f"- {ingredient}")

# Check if a recipe is selected and display details if so
if "selected_recipe_id" in st.session_state:
    # Get the recipe details from the session state using the recipe's _id
    selected_recipe_id = st.session_state.selected_recipe_id
    selected_recipe = next(r for r in recipes if str(r["_id"]) == selected_recipe_id)
    
    # Display selected recipe details
    st.write(f"### {selected_recipe['name']}")
    st.write(f"**Time:** {selected_recipe['cook_time']}")
    st.write(f"**Difficulty:** {selected_recipe['difficulty']}")
    
    
    # Display ingredients
    display_ingredients(selected_recipe['ingredients'])

    # Add a "Back" button to return to the grid view
    if st.button("Back to Recipes Grid"):
        # Reset session state to go back to grid
        del st.session_state.selected_recipe_id
        st.rerun()

else:
    # Display the recipe grid initially
    display_recipe_grid(recipes)
