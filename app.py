pip install streamlit pandas

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\Users\고병수\Desktop\부산광역시 동구_장애인일자리 현황_20221024.csv”)

# Streamlit app code
st.title("Graph App")

# Sidebar input selection
option = st.sidebar.selectbox("Select input", ['Welfare Center', 'Municipality'])

# Filter the data based on the selected option
if option == 'Welfare Center':
    filtered_data = data[data['Institution Type'] == 'Welfare Center for the Disabled']
else:
    filtered_data = data[data['Institution Type'] == 'Sigun-gu Busan Dong-gu Office']

# Plotting the graph
plt.plot(filtered_data['Year'], filtered_data['Assigned Personnel'])
plt.xlabel('Year')
plt.ylabel('Assigned Personnel')
st.pyplot()
