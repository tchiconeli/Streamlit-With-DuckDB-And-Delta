import streamlit as st
from duckdbClasses.quackActions import quackActions
from controller import tableObject
from helpers import helpers
from io import StringIO

  
    
    
def createOrDropTable(checkFlag: bool
                      ,tableName:str
                      ,url:str
                      ,docType:str
                      ,limit:int=100
                      ,uri:str="" 
                      ,container: st.container = None):
        if checkFlag:
            container.write(f"Creating table {tableName} ")
            match uri:
                case "obs": 
                    quackActions.setObsSecrets()
                    path = f"s3://{url}"
                    quackActions.execCreateTempTable(tableName=tableName,path=path,docType=docType,limit=limit,uri=uri )
            container.write(f"Table {tableName} was created.")
        else:
            container.write(f"Droping table {tableName} ")
            match uri:
                case "obs": 
                    quackActions.setObsSecrets()
                    quackActions.execDropTempTable(tableName=tableName)
            container.write(f"Table {tableName} was deleted.")
        
        
# def tableFlagChange(instance: tableObject.tableParameter):
def loadTables(instances: tableObject.tableForDuckdb,container):
    for instance in instances:
        createOrDropTable(checkFlag=True
                          ,tableName=instance.tableName
                          ,url=instance.url.replace("{partitionDate}",partitionDate)
                          ,docType=instance.docType
                          ,uri=instance.uri
                          ,limit=-1
                          ,container=container
                          )
        
        

def loadTablesInstances(object=None):
    loaders = []
    match object:
        case None: 
            dados = helpers.loadJsonTablesInternal()["loaders"]
            for load in dados:
                loader = tableObject.tableForDuckdb(**load)
                loaders.append(loader)
        case "str":
            dados = helpers.loadJsonFromString(object)["loaders"]
            st.write(dados)
            for load in dados:
                loader = tableObject.tableForDuckdb(**load)
                loaders.append(loader)
    return loaders 
       
partitionDate = st.text_input(label="insert partitionDate",value="*")


if st.button("Create From internal file"):
    with st.expander("Log create table"):
        container : st.delta_generator.DeltaGenerator = st.container(border=True,height=200)    
        listTableInstances = loadTablesInstances()
        loadTables(listTableInstances,container)
    
