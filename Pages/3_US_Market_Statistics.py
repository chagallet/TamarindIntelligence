import streamlit as st 
import pandas as pd 
import plotly.express as px
import Data

st.set_page_config(
    page_title="US Market Statistics"
)

st.title("Statistics for US Market")

df=Data.load_data()
custom_dict=Data.cust_dict()

# Creating a subgroup for US Market
REST = df.loc[(df.iloc[:,5]!= 'Geek Vape') & (df.iloc[:,5]!= 'SMOK')]

st.subheader("User Base Statistics")

st.write("##### Gender Distribution for US Customers & Products")
# Plotting the gender distribution for US Customers 
fig = px.histogram(REST, x="gender", title="Overall Gender Distribution")
st.plotly_chart(fig, use_container_width=True)

# Plotting the gender distribution per main hardware 
fig = px.histogram(REST, x="gender", color="main_hardware", title='Gender Distribution per Main Hardware')
st.plotly_chart(fig, use_container_width=True)

st.write("##### Age Group Distribution for US Customers & Products")
# Plotting the age group distribution for US Customers
fig = px.histogram(REST.sort_values(by='age_group'), x="age_group", title="Overall Age Group Distribution") 
st.plotly_chart(fig, use_container_width=True)

# Plotting the age distribution per main hardware 
fig = px.histogram(REST.sort_values(by='age_group'), x="age_group", color="main_hardware", title="Age Group Distribution per Main Hardware") 
st.plotly_chart(fig, use_container_width=True)

st.subheader("Market Position")

# Plotting the primary device distribution 
st.write("##### Primary Device Type Distribution sold in the US Market")
fig = px.histogram(REST, x="primary_device", title='Primary Device Distribution')
st.plotly_chart(fig, use_container_width=True)

# Plotting the main hardware distribution
st.write("##### Main Hardware Type Distribution sold in the US Market")
fig = px.histogram(REST, x="main_hardware", title='Main Hardware Distribution')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Customer Satisfaction")

# Plotting the satisfaction from US purchases 
fig = px.histogram(REST.sort_values(by='satisfaction'), x="satisfaction", title="Overall Satisfaction", category_orders=custom_dict) 
st.plotly_chart(fig, use_container_width=True)

# Plotting the satisfcation distribution per gender
fig = px.histogram(REST.sort_values(by='satisfaction'), x="satisfaction", color="gender", title="Satisfaction per Gender", category_orders=custom_dict) 
st.plotly_chart(fig, use_container_width=True)

# Plotting the satisfcation distribution per age group 
fig = px.histogram(REST.sort_values(by='satisfaction'), x="satisfaction", color="age_group", title="Satisfaction per Age Group", category_orders=custom_dict) 
st.plotly_chart(fig, use_container_width=True)

# Plotting the satisfcation distribution per primary device 
fig = px.histogram(REST.sort_values(by='satisfaction'), x="satisfaction", color="primary_device", title="Satisfaction per Primary Device", category_orders=custom_dict)
st.plotly_chart(fig, use_container_width=True)

# Plotting the satisfcation distribution per main hardware
fig = px.histogram(REST.sort_values(by='satisfaction'), x="satisfaction", color="main_hardware", title="Satisfaction per Primary Device", category_orders=custom_dict)
st.plotly_chart(fig, use_container_width=True)