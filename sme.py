import streamlit as st
import time
import pandas as pd
#mport matplotlib.pyplot as plt
from PIL import Image




st.title('SMART COMPTEL')

st.write("A group of computer companies bidding for contracts")
image = Image.open('sme_sales.jpg')
st.image(image,use_column_width="auto")

with st.expander("Read More..."):
                 st.write('The datasets includes group of companies who sells computers and  other computers services..The datatset contains the number of contract bids from each company and the quantity of products sold for each bid.')

sme_sales=pd.read_excel('sales.xlsx')

data_sme= pd.DataFrame(sme_sales)
st.dataframe(data_sme)

 #we need another colum to calculate the ammount of each sales rep
st.text('Lets calculate the cost of each products')
data_sme["Cost"] =data_sme["Quantity"]*data_sme["Price"]
st.dataframe([data_sme['Quantity'],data_sme['Price'],data_sme['Cost']])

st.text('Which product sold more or less?') 
prod_sme =data_sme.groupby('Product')['Quantity'].count()
st.dataframe(prod_sme)                            
st.bar_chart(prod_sme, width=150, height=300) 
st.write('CPU has the highest number of  sought out product while monitor is the least')

st.text('Which company got more contract bids?') 
sales_rep=data_sme['Name'].value_counts()
st.dataframe(sales_rep)
st.bar_chart(sales_rep)
st.text('Trantow barrows had more contract bids!')

st.text('Which of the companies won a contract?')
sme_won = data_sme['Status'] == 'won'
st.dataframe(data_sme[sme_won])




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 