import streamlit as st
import pandas as pd
import numpy as np
st.title("Amazon sales data analysis")


upload_file = st.file_uploader("Amazon dataset of sales",type=["csv"])

if upload_file:
    st.write("Dataset is uploaded")
    df = pd.read_csv(upload_file)
    df = df.rename(columns={"product_name":"Product Name"})
    df = df.rename(columns={"product_id":"Product Id"})
    df = df.rename(columns={"discounted_price":"Discounted Price"})   
    st.subheader("Amazon sales data")
    st.dataframe(df)
    Product_name = st.sidebar.text_input("Product Name")
    
    if Product_name :
        filtered_product = df[df["Product Name"].str.contains(Product_name,regex=False)] # regex removed the default interpreetations
        
        st.dataframe(filtered_product,width="content")
    else:
        st.warning("Product not found")
else:
        st.write("Please upload the CSV file of data set.")





