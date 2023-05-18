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
    compare_institutions = st.sidebar.checkbox("Compare Institutions")

    # Filter data for the selected institution type
    filtered_data = df[df['Institution Type'] == selected_institution_type]

    # Create chart
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        
        # Single institution graph
        if not compare_institutions:
            filtered_data.plot(x='year', y='Assigned Personnel', kind='bar', ax=ax)
            plt.xlabel('Year')
            plt.ylabel('Assigned Personnel')
            plt.title(f"Personnel Distribution for {selected_institution_type}")
        
        # Comparison graph for two institutions
        else:
            institutions = filtered_data['기관명'].unique()
            institution1 = st.sidebar.selectbox("Select Institution 1", institutions)
            institution2 = st.sidebar.selectbox("Select Institution 2", institutions)
            
            filtered_data1 = filtered_data[filtered_data['기관명'] == institution1]
            filtered_data2 = filtered_data[filtered_data['기관명'] == institution2]
            
            if not filtered_data1.empty and not filtered_data2.empty:
                fig, ax = plt.subplots()
                ax.bar(filtered_data1['year'], filtered_data1['Assigned Personnel'], label=institution1)
                ax.bar(filtered_data2['year'], filtered_data2['Assigned Personnel'], label=institution2)
                plt.xlabel('Year')
                plt.ylabel('Assigned Personnel')
                plt.title(f"Personnel Comparison for {selected_institution_type}")
                plt.legend()
            
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
