import streamlit as st

st.title("Visualise your current recipes")

recipes = [
    {"name": "Toast", "image": "assets/toastimage.jpg" },
    {"name": "Spaghetti", "image": "assets/toastimage.jpg" },
    {"name": "Burrito", "image": "assets/toastimage.jpg" },
    {"name": "Jollof Rice", "image": "assets/toastimage.jpg" }
]
#making a table
for recipe in recipes:
    column = st.columns([1,2]) # 2 columns
    with column[0]:
        st.image(recipe["image"],width=100)
    with column[1]:
        st.subheader(recipe["name"])