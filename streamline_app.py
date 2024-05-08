import streamlit as st
st.write("""
      requests
      
      pandas
      
      regex
      
      time
      
      datetime
      
      json
      
      logging
      
      os
      
      json
""")
import regex as re
import pandas as pd

df = pd.read_csv("2010-apr-MixComp.csv")
st.write(df.columns)
