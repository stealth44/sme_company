import streamlit as st
import time
import pandas as pd
#mport matplotlib.pyplot as plt
from PIL import Image




st.title('SMART LIGHT')

st.write("An SME that aims to illuminate the planet with solar panels!")
image = Image.open('sme_panels.jpg')
st.image(image, use_column_width="auto")

with st.expander("Read More..."):
                 st.write('A SME Company called SMART LIGHT specialized in selling panels possesses 5 subsidiaries across two continent namely in the cities New York, Los Angeles, London, Paris and Munich. These cities are internally referenced by thier codes C001,....C005, respectively. At the end of each quater, a subsidiary should communicate to the headquater the ammounts of sales and costs done during the quater, however, monthly detailed. Based on the communicated data, the head quaters wants to produce a quaterly that should entail statistics related to sales and profits done either individually or globally. These statistics should be helpful for eveluating the activities of each subsidiary and in making business decisions by the direction.')

sme_sales=pd.read_csv('sme.csv')


data_sme= pd.DataFrame(sme_sales)
st.table(data_sme)