import streamlit as st
import pandas as pd

# Проверка на загрузку файла
try:
    df = pd.read_excel('hoby.xlsx')
    st.write("Файл успешно загружен.")
except FileNotFoundError:
    # Если файла нет, создаем пустой DataFrame
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
            # Очистка кэша перед записью
            st.cache_data.clear()
            df.to_excel('hoby.xlsx', index=False)
            st.write('Вы записаны в базу')
        except Exception as e:
            st.write("Ошибка при записи в файл:", e)
else:
    st.write("Введите данные, чтобы добавить их в базу.")
