# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import datetime
import xgboost as xgb
import streamlit as st
import numpy as np

def main():
   import streamlit as st

# Define the HTML code to display
html_temp = """
<div style="background-color:lightblue;padding:20px">
<h1 style="color:black;text-align:center;font-size:50px;">Car Price Prediction Using ML</h1>
</div>
"""
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')
# Display the HTML code
st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.markdown("#### Are you planning to sell your car!?\n#### So Let's try to Evaluate the Price.")

p1 = st.number_input("What is the current Ex-Showroom price of the car",2.5,25.0,step=1.0)

p2 = st.number_input("What is the distance completed by the car in Miles?",100,500000,step=100)
 
s1 = st.selectbox("What is the Fuel type of the car?",('Petrol','Diesel','CNG'))   

if s1 == "Petrol":
    p3=0
elif s1 == "Diesel":
    p3=1
elif s1 == "CNG" :
    p3=2

s2 = st.selectbox("Are you a Dealer or Individual?",('Dealer','Individual'))   

if s2 == "Dealer":
    p4=0
elif s2 == "Individual":
    p4=1

s3 = st.selectbox("What is the Transmission Type?",('Manual','Automatic'))   

if s3 == "Manual":
    p5=0
elif s3 == "Automatic":
     p5=1   
     
p6 = st.slider("Number of Owners the car previously had?",0,3)

date_time=datetime.datetime.now()
years = st.number_input("In which year car was purchased?",1990,date_time.year)
p7 = date_time.year - years

import pandas as pd
data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])


if st.button('Predict'):
    pred = model.predict(data_new)
    st.balloons()
    st.success("You can sell your car for {:.2f} lakhs".format(float(pred)))





if __name__ == '__main__':
    main()





