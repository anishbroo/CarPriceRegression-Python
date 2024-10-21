import streamlit as st

col_1, col_2 = st.colums(2)
with col_1:



    value = 1
    if value > 1:
        st.write("Value is greater than 1")
    else:
        st.write("Value is less than 1")


st.sidebar.slider('age', 0, 110)
age=st.sidebar.slider('age', 0, 110)
with col_2:
    st.write(f"Value of age from slider is{age}")
