import streamlit as st
from duckdbClasses.quackActions import quackActions

def executeQuery(q:str):
    if q!="":
        with st.spinner("Processing:"):
            st.write("Result:")
            st.write(quackActions.execQueryToPandasDF(query))


query = st.text_area(label="Insert query",height=500,on_change = None)

if st.button("Execute Query"):
    executeQuery(query)

    
with st.expander("Tables:") :
    st.write(quackActions.execQueryExistingTables())

