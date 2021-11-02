import pandas as pd
import numpy as np
import streamlit as st
# Add an expander and display the dataset as a static table within the expander.
def app(df):
  st.header("View Data ")
  with st.beta_expander("View Dataset:"):
    st.table(df)
  st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(df.describe())
  beta_col1,beta_col2,beta_col3=st.beta_columns(3)
    with beta_col1:
      if st.checkbox("Show All Column Names"):
        st.table(list(df.columns))
    with beta_col2:
      if st.checkbox("View Column DataType"):
        st.table(df.dtypes)
    with beta_col3:
      if st.checkbox("View Column Data"):
        column_data=st.selectbox("Select Column",tuple(df.columns))
        st.write(df[column_data])