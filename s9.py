import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit 앱 제목
st.title("입력값에 따른 그래프")

# 사용자 입력: x축 값
x_values = st.number_input("x 값을 입력하세요:", min_value=1, max_value=100, value=10)

# 데이터 생성: y = x^2
y_values = [i**2 for i in range(1, x_values + 1)]

# 데이터프레임 생성
df = pd.DataFrame({'x': range(1, x_values + 1), 'y': y_values})

# 그래프 표시
st.line_chart(df.set_index('x'))

# Matplotlib 그래프 추가 (선택 사항)
plt.figure(figsize=(10, 5))
plt.plot(df['x'], df['y'], marker='o')
plt.title("y = x^2 그래프")
plt.xlabel("x 값")
plt.ylabel("y 값")
st.pyplot(plt)
