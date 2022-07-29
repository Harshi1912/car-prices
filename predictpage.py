import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_squared_log_error
def app(df):
	st.header('select desired values')
	cw=st.slider('car width',float(df['carwidth'].min()),float(df['carwidth'].max()))
	es=st.slider('engine size',float(df['enginesize'].min()),float(df['enginesize'].max()))
	hp=st.slider('horse power',float(df['horsepower'].min()),float(df['horsepower'].max()))
	dwf=st.radio('drivewheel fwd',[0,1])
	ccb=st.radio('car company buick',[0,1])


	if st.button('predict'):

		score,y_pred,mse,mae,msle=predict(df,cw,es,hp,dwf,ccb)
		st.success(f'THE PREDICED PRICE IS: ${np.round(y_pred,2)}')
		st.write('additional informtion: score=',score,'mean squared error=',mse,'mean absolute error=',mae,'mean absolute log error=',msle)
def predict(df,cw,es,hp,dwf,ccb):
	x=df[df.columns[:-1]]
	y=df['price']
	xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.33,random_state=44)
	lr=LinearRegression()
	lr.fit(xtrain,ytrain)
	score=lr.score(xtrain,ytrain)
	y_pred=lr.predict([[cw,es,hp,dwf,ccb]])
	y_test_pred=lr.predict(xtest)
	mse=mean_squared_error(ytest,y_test_pred)
	mae=mean_absolute_error(ytest,y_test_pred)
	msle=mean_squared_log_error(ytest,y_test_pred)
	return score,y_pred,mse,mae,msle


