import streamlit as st
st.title("All your recipes")

search_query = st.text_input("Search for recipe by name or ingredient")
if search_query:   #checking if the search query has information
 st.write({search_query})
 #example results- we will fetch this from our database when we make our query on mongodb
 st.write('- Toast')
 st.write('- Spaghetti')

#streamlit is very compatible with markdown so you can code as if your doing markdown on github-use st.markdown()

