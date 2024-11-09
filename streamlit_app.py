import streamlit as st
import pandas as pd
import os

# Укажите полный путь к файлу Excel
file_path = 'hoby.xlsx'

# Проверка загрузки файла
try:
    df = pd.read_excel(file_path)
    st.write("Файл успешно загружен.")
except FileNotFoundError:
    # Если файл не найден, создаем пустой DataFrame
    df = pd.DataFrame(columns=['full_name', 'Hoby'])
    st.write("Файл не найден. Создан новый DataFrame.")

# Ввод данных
name = st.text_input('Полное Имя')
hobby = st.text_input('Хобби')

# Добавляем проверку на пустые строки
if name and hobby:
    df2 = pd.DataFrame({'full_name': [name], 'Hoby': [hobby]})
    if st.button('Внести в базу'):
        # Конкатенация данных
        df = pd.concat([df, df2], ignore_index=True)
        
        # Проверка содержимого перед записью
        st.write("DataFrame для записи:", df)
        
        # Попытка записи в файл
        try:
            df.to_excel(file_path, index=False)
            st.write(f"Данные сохранены в файле: {file_path}")
            
            # Повторное чтение файла после записи
            updated_df = pd.read_excel(file_path)
            st.write("Содержимое файла после записи:")
            st.write(updated_df)
        except Exception as e:
            st.write("Ошибка при записи в файл:", e)
else:
    st.write("Введите данные, чтобы добавить их в базу.")
df = pd.read_excel(file_path)
st.write(df)
