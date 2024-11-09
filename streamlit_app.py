import streamlit as st
import pandas as pd 

df = pd.read_excel('hoby.xlsx')
name = st.text_input('Полное Имя')
hobby = st.text_input('Хобби')
df2 = pd.DataFrame({'full_name':name, 'Hoby':hobby})
if(st.button('Внести в базу')):
  df = pd.concat(df,df2)
  df.to_excel('hoby.xlsx')
  st.write('Вы записаны в базу')
