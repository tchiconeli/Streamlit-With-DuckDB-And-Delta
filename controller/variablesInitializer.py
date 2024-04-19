import streamlit as st
import os
from helpers import helpers

def envVariableInit():
    varAmbiente = list(os.environ.keys())
    for confKey,confValue in helpers.loadCloudEnviromentVariable().items():
        if confKey not in varAmbiente:
            key = confKey.upper()
            os.environ[key] = confValue
            print(f"Creating env variabel - {key} = {confValue}")

print("==================================")