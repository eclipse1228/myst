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
    show_ma = st.sidebar.checkbox("Show Moving Average")

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

        # Calculate moving average
        if show_ma:
            window = 2  # 이동 평균선의 기간 설정 (예시로 2년)
            assigned_personnel = filtered_data['Assigned Personnel']

#             # 이동평균 계산
#             moving_average = assigned_personnel.rolling(window).mean()

#             # 이동평균선 그래프 그리기
#             ax.plot(filtered_data['year'], moving_average.shift(-window+1), color='green', linestyle='--', label=f'{window}-year Moving Average')

#         # Calculate average and show average line
#         if show_average:
#             average_personnel = filtered_data.groupby('year')['Assigned Personnel'].mean()

#             # 평균선 그래프 그리기
#             ax.axhline(average_personnel.mean(), color='red', linestyle='--', label='Average')
if show_ma:
    window = 2  # 이동 평균선의 기간 설정 (예시로 2년)
    assigned_personnel = filtered_data['Assigned Personnel']

    # 이동평균 계산
    moving_average = assigned_personnel.rolling(window).mean()

    # 이동평균선 그래프 그리기
    ax.plot(filtered_data['year'].iloc[window-1:], moving_average, color='green', linestyle='--', label=f'{window}-Year Moving Average')



plt.legend()
st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

if __name__ == '__main__':
    main()
