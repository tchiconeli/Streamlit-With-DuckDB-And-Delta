import streamlit as st
import os
from controller import defaults

defaults.setDefaultDatabaseValueSession()

def setEnvValue(key:str, value,*args):
    print(args)
    os.environ[key] = value

with st.expander("OBS"):
    for k,v in list(os.environ.items()):
        if k.startswith('ST_OBS'):
            print(f'{k} = {v}')
            v = st.text_input(label=k,value=v,key=k)
            setEnvValue(k,v)
            
with st.expander("GCP (only for delta table)"):
    for k,v in list(os.environ.items()):
        if k.startswith('ST_GCP'):
            print(f'{k} = {v}')
            v = st.text_input(label=k,value=v,key=k)
            setEnvValue(k,v)

print("==========A=============")

