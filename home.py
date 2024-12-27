import streamlit as st
from urllib.parse import quote_plus
from pymongo import MongoClient

#connect to MongoDB
username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['recipe-book']
collection = db['recipes']

st.set_page_config(page_title="Home")

#Header
st.title("Recipe Book Project")
st.subheader("Discover, generate and store recipes")

#image
#st.image("assets/recipeimage2.jpg", use_container_width=True)   
st.image("assets/recipebook.jpg", width=1000 )



#Intro
st.markdown("## Welcome to your Recipe Book")
st.text("This is a recipe book where you can record your recipes, generate recipes based on your ingredients and.... ")

#Divider
st.divider()

#Call to Action
st.markdown("### Get Started")
st.write("Ready to dive into the world of delicious recipes?")


if st.button("Add a New Recipe"):
    st.page_link("pages/🍚_add_recipes.py", label="Add a New Recipe", icon=None, help=None, disabled=False, use_container_width=True)
    #st.write("Navigate to the 'Add Recipe' page to share your culinary creations!")
    
if st.button("Generate Recipes"):
    st.page_link("pages/🧞_generator.py", label="Generate Recipes", icon=None, help=None, disabled=False, use_container_width=True)
    #st.write("Navigate to the 'Generate' page to share your culinary creations!")

st.write("**You can also view your current recipes and search the recipes in this notebook**")

#Recently added preview card
st.markdown("### Recently added")
st.write("Your most recent recipes will show here:")

# Query to fetch the two most recent recipes
recent_recipes = list(collection.find().sort('created_at', -1).limit(2))


rows = 1
columns = 2

for row in range(rows):
    cols = st.columns(columns)
    for col_index, col in enumerate(cols):
        with col:
            container = st.container(border=True)
            with container:

                if row == 0 and col_index == 0:
                    st.write("🍲 **Latest Recipes**")
                    for recipe in recent_recipes:
                        recipe_name = recipe.get('name')
                        cooking_time = recipe.get('cook_time', 'N/A')  # Default value if not available
                        difficulty_level = recipe.get('difficulty', 'N/A')  # Default value if not available

                        # Display the recipe details
                        st.write(f"**{recipe_name}**")
                        st.write(f"⏱️ Cooking Time: {cooking_time} minutes")
                        st.write(f"🌟 Difficulty: {difficulty_level}")
                        st.write("---")
               

if len(recent_recipes) == 0:
    st.write("No recent recipes found.")
else:
    # Display "Latest Recipes" title
    st.write("🍲 **Latest Recipes**")

    # Create columns to display each recipe side-by-side in separate "cards"
    cols = st.columns(2)  # Create two columns for side-by-side display

    # Loop through the recipes and display each in its respective column
    for i, recipe in enumerate(recent_recipes):
        recipe_name = recipe.get('name', 'Unnamed Recipe')
        cooking_time = recipe.get('cook_time', 'N/A')  # Default value if not available
        difficulty_level = recipe.get('difficulty', 'N/A')  # Default value if not available

        # Use the appropriate column for each recipe (based on the index)
        with cols[i]:
            # Create a container for each recipe
            with st.container():
                # Display recipe info inside a card-like layout
                st.write(f"**{recipe_name}**")
                st.write(f"⏱️ Cooking Time: {cooking_time} minutes")
                st.write(f"🌟 Difficulty: {difficulty_level}")
                st.markdown("---")  # Add a horizontal line to separate recipes


#Stats/summary preview card
#st.markdown("### Stats/Summary") -don't have enough things recently to add to the stats card.
#total no of recipes added,



# Footer
st.markdown("---")
st.markdown("Made with Streamlit")