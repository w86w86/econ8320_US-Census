import streamlit as st
st.write("""
      
      json
""")

import pandas as pd
df = pd.read_csv("2010-apr-MixComp.csv")

st.write(f"""{df.columns}""")
