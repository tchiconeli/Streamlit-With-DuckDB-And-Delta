import streamlit as st
from duckdbClasses.quackActions import quackActions
from controler import tableObject
from helpers import helpers
from io import StringIO

    
def createOrDropTable(checkFlag: bool
                      ,tableName:str
                      ,url:str
                      ,docType:str
                      ,limit:int=100
                      ,uri:str="" ):
    if checkFlag:
        st.write(f"Creating table {tableName} ")
        match uri:
            case "obs": 
                quackActions.setObsSecrets()
                path = f"s3://{url}"
                quackActions.execCreateTempTable(tableName=tableName,path=path,docType=docType,limit=limit,uri=uri )
        st.write(f"Table {tableName} was created.")
    else:
        st.write(f"Droping table {tableName} ")
        match uri:
            case "obs": 
                quackActions.setObsSecrets()
                quackActions.execDropTempTable(tableName=tableName)
        st.write(f"Table {tableName} was deleted.")
        
        
# def tableFlagChange(instance: tableObject.tableParameter):
def loadTables(instances: tableObject.tableForDuckdb):
    for instance in instances:
        createOrDropTable(checkFlag=True
                          ,tableName=instance.tableName
                          ,url=instance.url.replace("{partitionDate}",partitionDate)
                          ,docType=instance.docType
                          ,uri=instance.uri
                          ,limit=-1
                          )
        
        

def loadTablesInstances(object=None):
    st.write(object)
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
            
    st.write(loaders)
    return loaders 
       
partitionDate = st.text_input(label="insert partitionDate",value="*")

                
if st.button("Create From internal file"):
    listTableInstances = loadTablesInstances()
    loadTables(listTableInstances)
