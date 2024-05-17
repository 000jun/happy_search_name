import streamlit as st
import pandas as pd

# 와이드페이지 설정
st.set_page_config(layout='wide')

# 헤더
st.header('이름 검색기 페이지', divider='rainbow')

# 데이터프레임 호출
df = pd.read_excel('secure_data_0517.xlsx')
df['last_number'] = df['last_number'].astype(str)

# 이름 입력
name = st.text_input(label='검색할 이름을 입력하시오.')

# 이름 검색 
condition = df['이름'] == name
result = df[condition]

# 결과 출력
st.write(f":orange[{name}]님의 번호는 :orange[{list(result['번호'].values)}]입니다.")
st.dataframe(result, width=800)
