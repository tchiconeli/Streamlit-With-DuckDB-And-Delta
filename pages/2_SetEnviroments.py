import streamlit as st
import os

def setEnvValue(key:str, value,*args):
    print(args)
    os.environ[key] = value

with st.expander("OBS"):
    for k,v in list(os.environ.items()):
        if k.startswith('ST_'):
            print(f'{k} = {v}')
            v = st.text_input(label=k,value=v,key=k)
            setEnvValue(k,v)

print("==========A=============")

