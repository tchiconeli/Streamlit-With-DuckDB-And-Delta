import streamlit as st
from duckdbClasses.quackActions import quackActions
from controller import defaults

defaults.setDefaultDatabaseValueSession()
    
if 'query' not in st.session_state:
    st.session_state['query'] = ""
    

def executeQuery(query:str):
    conn = quackActions.getConnection(st.session_state['databaseName'],readOnly=True)
    if query !="":
        with st.spinner("Processing:"):
            st.write("Result:")
            st.write(quackActions.execQueryToPandasDF(query,connection=conn) )


query = st.text_area(label="Insert query",height=500,on_change = None,value=st.session_state['query'])
st.session_state['query'] = query


if st.button("Execute Query"):
    executeQuery(query)

    
with st.expander("Tables:") :
    conn = quackActions.getConnection(st.session_state['databaseName'],readOnly=True)
    st.write(quackActions.execQueryExistingTables(st.session_state['databaseName'],connection=conn))

