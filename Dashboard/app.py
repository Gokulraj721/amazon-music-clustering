# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clustered_music_data.csv')

st.title("Amazon Music Clustering Dashboard")

cluster = st.selectbox("Select Cluster", sorted(df['cluster'].unique()))
filtered = df[df['cluster'] == cluster]

st.write(f"Songs in Cluster {cluster}", filtered.head())

st.subheader("Feature Distributions")
feature = st.selectbox("Select Feature", df.columns[:-1])  # exclude 'cluster'
sns.histplot(data=filtered, x=feature, kde=True)
st.pyplot(plt)
