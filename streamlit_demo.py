import streamlit as st
import numpy as np
import pandas as pd
import time

# Using st.title
st.title("My Streamlit App")

st.write("Here is my first attempt at using data to creat a table in Streamlit")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Using magic
"""
# My Streamlit app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# Showing chart data
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Showing map data
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Using a checkbox as a conditional statement
if not st.checkbox('Hide dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
"So you can just write?"

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("WOOHOO!")

expander = st.beta_expander("FAQ")
expander.write("Here you can put in some really long explanations about stuff if you like...")

st.sidebar.markdown("## This is markdown \n and this is also markdown after a linebreak and this is too \n # OK")

st.write("Starting a long computation...")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"And now we are done"



