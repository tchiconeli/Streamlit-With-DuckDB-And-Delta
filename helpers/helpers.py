import yaml
import os
import json

def loadYaml(file_path: str):
    with open(file_path) as f:
        return yaml.safe_load(f)
    
def loadJsonFromFile(file_path: str):
    with open(file_path, 'r') as arquivo:
        return json.load(arquivo)

def loadJsonFromString(json_string: str):
    js= json.loads(json_string)
    print(js)
    return js
    
def loadObsConf():
    print(f"=============================\n {__file__}")
    file_path = "confs\\obsConf.yaml"
    return loadYaml(file_path)

def loadJsonTablesInternal():
    print(f"=============================\n {__file__}")
    file_path = "confs\\tablesConf.json"
    print(f"=============================\n {file_path}")
    return loadJsonFromFile(file_path)
