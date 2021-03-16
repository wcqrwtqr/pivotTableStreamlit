import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021 / By Mohammed Albatati')
st.subheader('Table of sales')


df = pd.read_excel('data.xlsx', sheet_name='data', usecols='A:I')
df.dropna(inplace=True)
df['Sale'] = df['Price']*df['Qty']
df['Profit'] = df['Sale']*df['Margin']/100

# Pivot table
# pivot_df = df.groupby(["Gender", "Country"])[['Date','id','Client Age','Margin','Qty']].sum()

# lists
genders = ['Male', 'Female']
products = df['Product'].unique().tolist()
country = df['Country'].unique().tolist()
ages = df['Client Age'].unique().tolist()


# webpage selections
age_selection = st.slider('Age:', min_value=min(ages), max_value=max(ages),
                          value=(min(ages), max(ages)))

product_selection = st.multiselect('product:', products, default=products)

country_selection = st.multiselect('Countries:', country, default=country)
gender_selection = st.multiselect('Gender', genders, default=genders)

# mask
gender_mask = df['Gender'].isin(gender_selection)
product_mask = df['Product'].isin(product_selection)
country_mask = df['Country'].isin(country_selection)
age_mask = df['Client Age'].between(*age_selection)
# product_mask = df['Product'].isin(['A'])
masked_df = (df['Gender'].isin(gender_selection) & df['Product'].isin(product_selection) & df['Client Age'].between(*age_selection) & df['Country'].isin(country_selection))

number_of_results = df[masked_df].shape[0]

# ---------
# df.groupby(by=['xxx']).count()[[yyy]]

pivot_df = df[masked_df].groupby(["Country", "Product"])[['Profit',
                                                          'Sale']].sum()

# Tables view on page
st.markdown(f'*Available Results: {number_of_results}')
# st.dataframe(df[masked_df])
# st.dataframe(pivot_df)

st.dataframe(df[masked_df])
st.dataframe(pivot_df)

# col1, col2 = st.beta_columns(2)

bar_chart = px.bar(pivot_df, x='Profit', y='Sale', text='Sale',
                   color_discrete_sequence=['#F63366']*len(pivot_df),
                   template='plotly_white')
st.plotly_chart(bar_chart)

image = Image.open('vim-logo.png')
# st.image(image, caption='Vim', use_column_width=True)
st.image(image, caption='Vim', width=200)





