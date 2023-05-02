import streamlit as st 
import pandas as pd 

def load_data():
    data = pd.read_excel("/Users/charlottegallet/Documents/Travail/Consumer survey task.xlsx")
    data = data.rename(columns={'What is your gender?':'gender','Which age group do you belong to?':'age_group','Which category your current PRIMARY device belongs to? (the device you use the most often)':'primary_device', 'Please select the piece of MAIN hardware that you last purchased (at least within 3 months).':'main_hardware', 'What was the brand of this piece of HARDWARE? Please select only one':'brand', 'Please rate from 1 (Not at all) to 10 (Very) how satisfied you are with this piece of hardware.':'satisfaction'})
    data.iloc[:,6]=data.iloc[:,6].replace('10=Very satisfied','10')
    data.iloc[:,6]=data.iloc[:,6].replace('1=Not at all satisfied','1')
    data.iloc[:,6]=data.iloc[:,6].astype(str)
    data.iloc[:,5]=data.iloc[:,5].replace('I canÂ´t remember', 'No Brand')
    data.iloc[:,5].fillna("No Brand", inplace=True)
    data.iloc[:,6].fillna("No Rating", inplace=True)  
    return data

def cust_dict():
    custom_dict = dict(satisfaction=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    #{'1': 0, '2': 1, '3': 2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9}
    return custom_dict



