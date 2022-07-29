
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse',False)
def app(df):
	st.header('Visualisation')
	st.subheader('scatter plots')
	var=st.selectbox('choose one feature',list(df.columns[:-2]))
	plt.figure(figsize=(15,5))
	plt.scatter(df[var],df['price'])
	st.pyplot()
	var1=st.multiselect('Other Graphs',['boxplot','histogram','correlation heatmap'])
	if 'boxplot' in var1:
		select=st.radio('choose one feature',tuple(df.columns[:-2]))
		plt.figure(figsize=(15,5))
		sns.boxplot(df[select])
		st.pyplot()
	if 'histogram' in var1:
		sell=st.radio('choose feature',list(df.columns[:-2]))
		plt.figure(figsize=(15,5))
		plt.hist(df[sell])
		st.pyplot()
	if 'correlation heatmap' in var1:
		
		plt.figure(figsize=(15,5))
		sns.heatmap(df.corr(),annot=True)
		st.pyplot()



