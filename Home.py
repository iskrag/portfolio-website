import streamlit as sl
import pandas as pd

sl.set_page_config(layout='wide')

col1, col2 = sl.columns(2)

with col1:
    sl.image('images/photo.jpg', width=300)

with col2:
    sl.title('Iskra Georgieva')
    content = ''' Hi, I am Iskra!'''
    sl.info(content)

content2 = 'Below you can find some of the apps I have built in Python. Feel free to contact me!'
sl.write(content2)

col3, empty_col, col4 = sl.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        sl.header(row['title'])
        sl.write(row['description'])
        sl.image('images/' + row['image'])
        sl.write(f"[SourceCode]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        sl.header(row['title'])
        sl.write(row['description'])
        sl.image('images/'+row['image'])
        sl.write(f"[SourceCode]({row['url']})")
