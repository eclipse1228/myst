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

    filtered_data = df[df['Institution Type'] == selected_institution_type]

    # Select institutions for comparison
    institution1 = st.sidebar.selectbox("Select Institution 1", filtered_data['기관명'].unique())
    institution2 = st.sidebar.selectbox("Select Institution 2", filtered_data['기관명'].unique())

    # Filter data for the selected institutions
    filtered_data1 = filtered_data[filtered_data['기관명'] == institution1]
    filtered_data2 = filtered_data[filtered_data['기관명'] == institution2]

    # Create comparison chart
    if not filtered_data1.empty and not filtered_data2.empty:
        fig, ax = plt.subplots()
        ax.bar(filtered_data1['year'], filtered_data1['number of participants assigned'], label=institution1)
        ax.bar(filtered_data2['year'], filtered_data2['number of participants assigned'], label=institution2)
        plt.xlabel('Year')
        plt.ylabel('Assigned Personnel')
        plt.title(f"Comparison of {institution1} and {institution2} ({selected_institution_type})")
        plt.legend()
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
