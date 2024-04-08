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
    file_path = os.path.join(os.path.dirname(__file__), "obsConf.yaml")
    return loadYaml(file_path)

def loadJsonTablesInternal():
    file_path = os.path.join(os.path.dirname(__file__), "tablesConf.json")
    return loadJsonFromFile(file_path)