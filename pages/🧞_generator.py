import openai
import streamlit as st


st.title("Recipe Generator")
st.subheader("Generate recipes based on ingredients you have available.")

# Set your OpenAI API key

openai.api_key = st.secrets[openai]["OPENAI_API_KEY"]


# Debugging the secrets
if "myap" in st.secrets:
    st.write("API Key loaded successfully!")
else:
    st.error("OPENAI_API_KEY not found in secrets!")


system_prompt = "Give me two recipe options based on ingredients the user gives.Only use the ingredients given, feel free to add seasonings if not added by the user."

recipe_valid = 0
messages = [
    {"role": "system", "content": system_prompt},
]

#User input
user_input = st.text_input("Enter ingredients (comma-separated):", key="user_input")
if user_input:
   user_message = {"role": "user", "content": user_input}
   messages.append(user_message)
   
#Recipe suggestions
with st.spinner("Generating recipes...."):
    response = openai.chat.completions.create(model = "gpt-3.5-turbo",  messages = messages)
gpt_content = response.choices[0].message.content
st.write("### Here are your recipes: ")
st.write(gpt_content)

#Asking if recipes are valid

st.write("**Can you make this recipe with the ingredients you entered?**")
if st.button("Yes"):
     st.success("Great! Enjoy your meal! 🎉")
elif st.button("No"):
    st.warning("The recipe cannot be made with the given ingredients.")

# Option to add more ingredients or regenerate
add_more = st.radio(
     "What would you like to do?",
     ["Add more ingredients", "See another recipe"]
     )

if add_more == "Add more ingredients":
    additional_ingredients = st.text_input("Enter additional ingredients:", key="additional_input")
    if additional_ingredients:
# Update user input and regenerate recipes
        updated_input = user_input + ", " + additional_ingredients
        messages.append({"role": "user", "content": updated_input})
        st.experimental_rerun()
    elif add_more == "See another recipe":
         messages.append({"role": "user", "content": "Try another recipe using the same ingredients."})
         st.experimental_rerun()

      