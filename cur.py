import streamlit as st
import numpy as np
import pandas as pd

st.title('Currency Converter')
currency = ['NGN','USD','JPY','CAD','GBP']

amt = st.number_input('Amount',min_value=0.0)
cur_f = st.selectbox('From',currency)
cur_t = st.selectbox('To',currency)


conv = [1, 0.00075, 0.12, 0.001, 0.00059]

def curr_converter(amt,cur_f,cur_t):
    ind_f = currency.index(cur_f)
    ind_t = currency.index(cur_t)

    rate_f = conv[ind_f]
    rate_t = conv[ind_t]

    value = amt * (rate_t/rate_f)
    value = round(value,2)
    return value

if st.button('Convert'):
    value = curr_converter(amt,cur_f,cur_t)
    st.success(f'')
