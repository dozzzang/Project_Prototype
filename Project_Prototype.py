# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import streamlit as st
# %matplotlib inline


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from bokeh.plotting import figure, show
warnings.filterwarnings("ignore")

# +
st.header('과거 10개년 데이터')
option = st.selectbox(
     '어느 년도의 데이터를 보고 싶으세요?',
     ('2013', '2014', '2015','2016','2017','2018','2019','2020','2021','2022'))

st.write(option,'년의 데이터입니다.')
# -

file_path = 'C:\\Users\\김도현\\lecturespace\\data-set.csv'
population_df = pd.read_csv(file_path,names = ['년도','출생아 수(명)','사망자 수(명)'])
population2_df = pd.read_csv(file_path,names=['년도','15~64살 생산연령인구(명)','65세 이상 고령인구(명)'])

st.bar_chart(x = "년도",data = population_df)

st.header('당신이 살게 될 미래의 대한민국이 궁금하지 않으세요?')
st.write('나이를 입력해보세요! 미래를 보여드립니다.')
number = st.number_input('나이 입력(1~60)',1,60)
st.write(number,'살이시군요!')

st.header('5년 뒤입니다.')
st.bar_chart(x = "년도",data = population2_df)
st.write(number+5,'살이시니 예상되는 사회 변화는')
st.write('~~ 분야 : ~~')
st.header('10년 뒤입니다.')
st.bar_chart(x = "년도",data = population2_df)
st.write(number+10,'살이시니 예상되는 사회 변화는')
st.write('~~ 분야 : ~~')
st.header('20년 뒤입니다.')
st.bar_chart(x = "년도",data = population2_df)
st.write(number+20,'살이시니 예상되는 사회 변화는')
st.write('~~ 분야 : ~~')


