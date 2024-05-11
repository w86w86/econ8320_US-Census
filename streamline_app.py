#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


st.write("""
      
      json
""")

import pandas as pd
df = pd.read_csv("2010-apr-MixComp.csv")

st.write(f"""{df.columns}""")
