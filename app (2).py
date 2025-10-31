import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PhonePe Data Dashboard", layout="wide")

st.title("📊 PhonePe Data Analytics Dashboard")
st.write("Analyzing digital payment trends across India 💜")


df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='active cases',
    color_continuous_scale='Viridis'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()

