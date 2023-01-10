import streamlit as st
import pandas as pd 
import numpy as np

df = pd.read_csv('life_expectancy_years.csv', index_col = 0 )
# print(df)
df_korea = df.loc['South Korea']

meanlife = np.round(np.mean(df_korea))
# print(meanlife)
years = pd.to_numeric(df_korea.index)
# print(years)

# Streamlit component, layout 구성하기

st.title("Life Expectancy of Korea")
st.line_chart(df_korea)

# slider input을 통한 숫자 입력 

number = st.slider(
    label = "Choose Number: ",
    min_value = int(np.min(years)),
    max_value = int(np.max(years)),
    step = 1
)

number2 = int(df_korea.loc[[str(number)]])

col1,col2 = st.columns(2)
with col1:
    st.metric(label = 'Mean life expectancy: All time',
          value = meanlife)
with col2:
    st.metric(label = 'Life Expectancy of selected year',
          value = number2,
          delta = number2 - meanlife)
    
    

# st.metric(label = 'Mean life expectancy: All time',
#           value = meanlife)

# st.metric(label = 'Life Expectancy of selected year',
#           value = number2,
#           delta = number2 - meanlife)
