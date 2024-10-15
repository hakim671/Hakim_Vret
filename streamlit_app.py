import streamlit as st

year = st.number_input("Возраст",value=10)
ves = st.number_input("Вес",value=30, step=10)
rost = st.number_input("Рост",value=150, step=10)
if st.button("Начать прогноз"):
  st.write("Zoir Гей")
