# 스트림릿 app.py 파일 생성
%%writefile app.py

# streamlit 라이브러리 불러오기
import streamlit as st

st.title('dsfds')                       # 제목 쓰기

st.subheader('jkhkj')         # 부제목 쓰기

st.write('fdvd')                  # 본문 쓰기

col1, col2 = st.columns(2)       # 여러 개의 열(문단)을 생성
with col1:
       st.write('A')
with col2:
       st.write('B')

#st.image( '____________' )              # 이미지 불러오기

a = st.number_input('수를 입력하세요', min_value=0)   # 사용자의 입력을 받아서 a에 저장하기(최소값은 0)

if a > 0:
      st.write('양수입니다')
elif a<0:
      st.write('음수입니다')
else:
      st.write('0입니다')
