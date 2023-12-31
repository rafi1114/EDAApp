import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



st.markdown('''

# **Exploratory Data Analysis Solution**
            
Making your life easy while working with Data


''')

with st.sidebar.header('1. Upload Your CSV Data'):
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    st.sidebar.markdown('''
[Example CSV Input File](https://github.com/rafi1114/EDAApp/blob/main/Different_stores_dataset.csv)
''')
    
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Your Dataframe**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profile Report**')
    st_profile_report(pr)

else:
    st.info('Awaiting Upload')
    if st.button('Press to use Example Dataset'):

        @st.cache_data
        def load_csv():
            csv = pd.read_csv('Different_stores_dataset.csv')
            return csv
        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Example Dataframe**')
        st.write('*This is an example dataset of different store and their customers.*')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profile Report**')
        st_profile_report(pr)