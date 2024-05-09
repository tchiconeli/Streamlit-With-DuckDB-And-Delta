import streamlit as st
from duckdbClasses.quackActions import quackActions
from controller import tableObject
from helpers import helpers
from io import StringIO
from controller import defaults

defaults.setDefaultDatabaseValueSession()

def createOrDropTable(checkFlag: bool
                      ,database:str
                      ,tableName:str
                      ,url:str
                      ,uri:str
                      ,docType:str
                      ,schema:str 
                      ,limit:int=100 
                      ,container: st.container = None):
        conn = quackActions.getConnection(database)
        if checkFlag:
            container.write(f"Creating table {schema}.{tableName} ")
            match uri:
                case "obs": 
                    quackActions.setObsSecrets(connection=conn)
                    path = f"s3://{url}"
                    quackActions.execCreateTempTable(tableName=tableName,path=path,docType=docType,limit=limit,uri=uri,schema = schema,connection = conn )
                case _:
                    path = f"{uri}://{url}"
                    quackActions.execCreateTempTable(tableName=tableName,path=path,docType=docType,limit=limit,uri=uri,schema = schema,connection = conn )
            container.write(f"Table {schema}.{tableName} was created.")
        else:
            container.write(f"Droping table {schema}.{tableName} ")
            match uri:
                case "obs": 
                    quackActions.setObsSecrets(connection=conn)
                    quackActions.execDropTempTable(tableName=tableName,connection=conn)
            container.write(f"Table {schema}.{tableName} was deleted.")
        
        
# def tableFlagChange(instance: tableObject.tableParameter):
def loadTables(instances: tableObject.tableForDuckdb,container):
    for instance in instances:
        createOrDropTable(checkFlag=True
                          ,tableName=instance.tableName
                          ,url=instance.url.replace("{partitionDate}",partitionDate)
                          ,schema= instance.schema
                          ,docType=instance.docType
                          ,uri=instance.uri
                          ,limit=instance.limitDataframe
                          ,container=container
                          ,database=databaseName
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
databaseName = st.text_input(label="insert Database name",value=st.session_state['databaseName'])

st.session_state['databaseName'] = databaseName

if st.button("Create From internal file"):
    with st.expander("Log create table"):
        container : st.delta_generator.DeltaGenerator = st.container(border=True,height=200)    
        listTableInstances = loadTablesInstances()
        loadTables(listTableInstances,container)
    
