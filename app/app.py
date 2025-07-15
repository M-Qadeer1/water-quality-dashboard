import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Water Quality Dashboard', layout='wide')

st.title("💧 Water Quality Data Dashboard")
uploaded_file = st.file_uploader("Upload your water quality CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    parameter = st.selectbox("Select Parameter to Visualize", df.columns[1:])
    fig = px.line(df, x=df.columns[0], y=parameter, title=f"{parameter} Over Time")
    st.plotly_chart(fig, use_container_width=True)
