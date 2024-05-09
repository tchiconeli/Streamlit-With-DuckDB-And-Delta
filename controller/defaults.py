import streamlit as st



def setDefaultDatabaseValueSession():
    if 'databaseName' not in st.session_state:
        st.session_state['databaseName'] = ':default:'
    else:
        print(st.session_state['databaseName'])
    