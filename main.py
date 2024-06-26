import streamlit as st
from controller import defaults
from controller.variablesInitializer import envVariableInit

defaults.setDefaultDatabaseValueSession()
    
st.write("# Pagina inicial")

st.write("## Talvez algum dia coloque algo util aqui")

st.write("Link streamlit: [Streamlit](https://docs.streamlit.io/get-started)")
st.write("Link duckdb: [Duckdb](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=win&download_method=package_manager)")

envVariableInit()