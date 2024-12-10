import streamlit as st

st.set_page_config(page_title="Home")

#Header
st.title("Recipe Book Project")
st.subheader("Discover, generate and store recipes")

#image
st.image("assets/recipeimage.jpg", use_container_width=True)   

#Intro
st.markdown("## Welcome to your Recipe Book")
st.text("This is a recipe book to generate recipes using AI. Record recipes you'll love to try again.")

#Divider
st.divider()


# Footer
st.markdown("---")
st.markdown("Made with Streamlit")