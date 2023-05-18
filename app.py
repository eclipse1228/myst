import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('job23.csv')

def main():
    st.title("기관 데이터 차트")
    st.sidebar.title("Chart Options")

    # Filter options
    institution_types = df['기관유형'].unique()
    selected_institution_type = st.sidebar.selectbox("기관유형", institution_types)

    filtered_data = df[df['기관유형'] == selected_institution_type]

    # Create chart
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        filtered_data.plot(x='연도', y='배정인원', kind='bar', ax=ax)
        plt.xlabel('연도')
        plt.ylabel('배정인원')
        plt.title(f"Personnel Distribution by Year for {selected_institution_type}")
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
