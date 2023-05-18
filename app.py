import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# CSV 파일을 Pandas DataFrame으로 로드합니다.
df = pd.read_csv('job23.csv')

def main():
    st.title("기관 데이터 차트")
    st.sidebar.title("차트 옵션")

    # 필터 옵션
    years = df['Year'].unique()
    selected_year = st.sidebar.selectbox("년도 선택", years)

    months = [
        '1월', '2월', '3월', '4월', '5월', '6월',
        '7월', '8월', '9월', '10월', '11월', '12월'
    ]
    selected_month = st.sidebar.selectbox("월 선택", months)

    institution_types = df['Institution type'].unique()
    selected_institution_type = st.sidebar.selectbox("기관 유형 선택", institution_types)

    filtered_data = df[
        (df['Year'] == selected_year) &
        (df['Month'] == selected_month) &
        (df['Institution type'] == selected_institution_type)
    ]

    # 차트 생성
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        filtered_data.plot(x='Institution name', y='Number of assigned personnel', kind='bar', ax=ax)
        plt.xlabel('기관 이름')
        plt.ylabel('배정된 인원 수')
        plt.title(f"{selected_year}년 {selected_month} {selected_institution_type}의 인원 분포")
        st.pyplot(fig)
    else:
        st.warning("선택한 필터에 대한 데이터가 없습니다.")

if __name__ == '__main__':
    main()
