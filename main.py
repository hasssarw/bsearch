import pandas as pd
import streamlit as st
pd.set_option('display.max_colwidth', -1)
st.set_page_config(layout="wide")


def make_clickable(link):
	# target _blank to open new window
	# extract clickable text to display for your link
	text = link.split('=')[0]
	return f'<a target="_blank" href="{link}">{text}</a>'

def path_to_image_html(path):
    return '<img src="' + path + '" width="300" >'



df = pd.read_csv('results.csv')
df['url'] = df['url'].apply(make_clickable)
df['image'] = df['image'].apply(path_to_image_html)
df = df[['brand','name','url','price','rrp','image']]

st.title('TKMaxx Brand Search')


listofbrands = df['brand'].unique()

choice = st.selectbox('pick brand', listofbrands)

# st.dataframe(df.loc[df['brand']==choice])
st.write(df.loc[df['brand']==choice].to_html(escape=False, index=False), unsafe_allow_html=True)