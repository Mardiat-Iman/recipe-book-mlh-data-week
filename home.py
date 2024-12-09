import streamlit as st

st.set_page_config(page_title="Home")

#title
st.title("Recipe Book Project")
#Divider
st.divider()
#image
st.image("assets/recipeimage.jpg", use_container_width=True)   

st.text("This is a recipe book to generate recipes using AI")

st.subheader("Learn how to generate recipes")
