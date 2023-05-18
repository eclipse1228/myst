import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
# Load the CSV file into a Pandas DataFrame




df = pd.read_csv('job23.csv')

def main():
    st.title("Busan Jobs for Disabled People")
    st.sidebar.title("Chart Options")

    # Filter options
    institution_types = df['Institution Type'].unique()
    selected_institution_type = st.sidebar.selectbox("Institution Type", institution_types)
    
    months = ['1월', '2월', '3월', '4월', '5월']
    selected_months = st.sidebar.multiselect("Select Months", months)

    filtered_data = df[
        (df['Institution Type'] == selected_institution_type) &
        (df['월'].isin(selected_months))
    ]
    
    # Create chart
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        filtered_data.plot(x='year', y='Assigned Personnel', kind='bar', ax=ax)
        plt.xlabel('year')
        plt.ylabel('Assigned Personnel')
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
