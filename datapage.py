
import numpy as np
import pandas as pd
import streamlit as st
def app(df):
	with st.expander('view data'):
			st.table(df)
	st.header('DATA DESCRIPTION')
	if st.checkbox('show'):
		st.table(df.describe())
	col1,col2=st. columns(2)
	with col1:
		if st.checkbox('show column names'):
			st.table(df.columns)
	with col2:
		if st.checkbox('show column data types'):
			st.write(list(df.dtypes))

