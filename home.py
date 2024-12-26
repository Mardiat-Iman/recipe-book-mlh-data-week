import streamlit as st

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

rows = 1
columns = 2

# for row in range(rows):
#     cols = st.columns(columns)
#     for col_index, col in enumerate(cols):
#         with col:
#             container = st.container(border=True)
#             with container:
#                 if row == 0 and col_index == 1:
#                     st.write("🍲 **Recipes**")
#                     st.write("1. Add new recipes with detailed instructions and images.")
#                     st.write("2. Browse through a variety of recipes shared by the community.")
#                     st.write("3. Get personalized recipe recommendations based on your preferences.")
#                     st.write("4. Rate and review recipes to help others find the best dishes.")
#                 elif row == 0 and col_index == 0:
#                     st.write("🍽️ **Add a New Recipe**")
#                     st.write("1. Share your favorite recipes with the community.")
#                     st.write("2. Fill out the form with the recipe name, ingredients, and instructions.")
#                     st.write("3. Upload an image of the dish to make it visually appealing.")
#                     st.write("4. Submit your recipe and inspire others to try it out.")
                

#Stats/summary preview card
st.markdown("### Stats/Summary")


# Footer
st.markdown("---")
st.markdown("Made with Streamlit")