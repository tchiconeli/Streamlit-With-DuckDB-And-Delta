import streamlit as st
from duckdbClasses.quackActions import quackActions

quackActions.setObsSecrets()

query = st.text_area(label="Insert query",height=500)

if query!="":
    with st.spinner("Processing:"):
        st.write("Result:")
        st.write(quackActions.execQueryToPandasDF(query))
    
with st.expander("Tables:") :
    # st.write("Tables existentes:")
    st.write(quackActions.execQueryToPandasDF("select table_catalog,table_schema,table_name from information_schema.tables"))

