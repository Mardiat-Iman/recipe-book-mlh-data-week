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

#Title
st.title("Visualise your current recipes")

#making a table 
for recipe in recipes:
    column = st.columns([1,2]) # 2 columns
    with column[0]:
        st.image(recipe["image"],width=100)
    with column[1]:
        st.subheader(recipe["name"])

#grid layout for recipes . Another way to layout the recipes
# for i in range(0, len(recipes), 2):
#     column = st.columns(2)
#     for column, recipe in zip(column, recipes[i : i +2]):
#         with column:
#             st.markdown(f"""
#                <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px;">
#                     <h3 style="text-align: center;">{recipe["name"]}</h3>
#                 </div>
#             """, unsafe_allow_html=True)
#             st.image(recipe["image"],width=100)

#footer
st.markdown("---")   
st.markdown("Made using Streamlit")                    

