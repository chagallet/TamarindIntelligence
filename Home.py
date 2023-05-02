import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Executive Summary"
)

st.title("Consumer Insights Geek Vape - US Market")
st.markdown(
    """
    Welcome to the executive summary page for the consumer insights for Geek Vape at the US market. 

    You will find on this page an executive summary with the key elements that have been discovered through a primary analysis. 
    On the side tabs you will also find graphs and visualisations for each Geek Vape, SMOK and the overall US Market. 
    """
)
st.subheader("Key Insights")
st.markdown(
    """
    Concerning the E-cigarette Market and Geek Vape's position in the US Market some key elements can be found

    - Overall there 452 customers who use Geek Vape's products 

    - From this sample, 70% are male, 29% are female and the rest prefers not to say.

    - The age group where Geek Vape is the most popular is for customers between 45 and 49 years-old, with 15.5%

    - The majority of the customers use Geek Vape for their advanced open system as their primary device and 65% of the customers use the box mod as their main hardware. 

    - 68% of Geek Vape's customers estimated their satisfaction at the highest level 10, meaning that they are very satisfied with the products. 

    - The satisfaction is also at the highest level when segmenting the customers per various groups such as the age or the device they use. 
    """
)

st.subheader("Conclusions")
st.markdown(
    """
    Some conclusions can be taken from the analysis. 

    - The other biggest player in the US Market is SMOK with 324 entries in the survey. 
     
    - From these 324 customers, it is possible to see that the satisfaction is also high, but the proportions for rating as 8 and 9 are higher than for Geek Vape. 

    - Overall, in the US Market, customers tend to use E-cigarettes in the form of Box Mod and are generally highly satisfied with the brands and products. 
    """
)




