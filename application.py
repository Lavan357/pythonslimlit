import streamlit as st
import pandas as pd

st.title("Simple Streamlit App")

st.write("This is a basic Streamlit application demonstrating dependencies.")

# Example of using pandas
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)
st.dataframe(df)

st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:")
if name:
    st.sidebar.write(f"Hello, {name}!")
