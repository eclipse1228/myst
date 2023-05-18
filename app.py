import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
# Load the CSV file into a Pandas DataFrame
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('font.family', 'NanumGothic')
mpl.rc('font', family='NanumGothic')

df = pd.read_csv('job23.csv', encoding='utf-8-sig')

def main():
    st.title("Busan Jobs for Disabled People")
    st.sidebar.title("Chart Options")

    # Filter options
    institution_types = df['Institution Type'].unique()
    selected_institution_type = st.sidebar.selectbox("Institution Type", institution_types)

    filtered_data = df[df['Institution Type'] == selected_institution_type]

    # Create chart
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        filtered_data.plot(x='year', y='Assigned Personnel', kind='bar', ax=ax)
        plt.xlabel('year')
        plt.ylabel('Assigned Personnel')
        plt.title(f"{selected_institution_type}")
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
