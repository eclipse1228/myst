import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('job23.csv')

def main():
    st.title("Busan Jobs for Disabled People")
    st.sidebar.title("Chart Options")

    # Filter options
    institution_types = ['시군구', '장애인복지관']
    selected_institution_type = st.sidebar.selectbox("Institution Type", institution_types)
    show_average = st.sidebar.checkbox("Show Average")

    # Filter data for the selected institution type
    filtered_data = df[df['Institution Type'] == selected_institution_type]

    # Create chart
    if not filtered_data.empty:
        fig, ax = plt.subplots()

        # Single institution graph
        filtered_data.plot(x='year', y='Assigned Personnel', kind='bar', ax=ax)
        plt.xlabel('Year')
        plt.ylabel('Assigned Personnel')
        plt.title(f"Personnel Distribution for {selected_institution_type}")

        # Show average line
        if show_average:
            average_personnel = filtered_data.groupby('year')['Assigned Personnel'].mean()
            ax.axhline(average_personnel.mean(), color='red', linestyle='--', label='Average')

        plt.legend()
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
