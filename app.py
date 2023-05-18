import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('job23.csv',encoding='utf-8')

def main():
    st.title("기관 데이터 차트")
    st.sidebar.title("차트 옵션")

    # Filter options
    years = df['연도'].unique()
    selected_year = st.sidebar.selectbox("연도 선택", years)

    months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
    selected_month = st.sidebar.selectbox("월 선택", months)

    institution_types = df['기관유형'].unique()
    selected_institution_type = st.sidebar.selectbox("기관유형 선", institution_types)

    filtered_data = df[
        (df['연도'] == selected_year) &
        (df['1월'] == selected_month) & 
        (df['기관유형'] == selected_institution_type)
    ]

    # Create chart
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        filtered_data.plot(x='기관명', y='배정인원', kind='bar', ax=ax)
        plt.xlabel('기관명')
        plt.ylabel('배정인원')
        plt.title(f"Personnel Distribution of {selected_institution_type} in {selected_month} {selected_year}")
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
