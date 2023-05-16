import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.radio(’Pick’ [장애인복지관,시군구])

st.selectbox(’장애인복지관’,[’male’,’시군구’])

st.radio(’Year’,[2018,2019,2020,2021,2022])

st.selectbox(’Year’,[2018,2019,2020,2021,2022])

data = pd.read_csv(’C:\Users\고병수\Desktop\부산광역시 동구_장애인일자리 현황_20221024.csv’)

plt.plot(data['월'], data['사람수'])
plt.xlabel('월')
plt.ylabel('')
st.pyplot()
