import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="PhonePe Data Dashboard", layout="wide")

st.title("📊 PhonePe Data Analytics Dashboard")
st.write("Analyzing digital payment trends across India 💜")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of data:")
    st.dataframe(df.head())

    if 'State' in df.columns and 'Transaction_amount' in df.columns:
        fig = px.choropleth(
            df,
            geojson="https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json",
            locations="State",
            color="Transaction_amount",
            title="State-wise Transaction Analysis"
        )
        st.plotly_chart(fig)
else:
    st.info("👆 Upload a dataset to see visualizations")

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

st.plotly_chart(fig)







