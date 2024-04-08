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
       
 

tupleProcess = ()    

tableItemSoldName = "item_sold"
tableProductName = "product"
tableProductSegment = "product_segment"
tableProductDelta = "product_delta"
tableFVendasEspandidoDelta = "fVendas_expandido"


partitionDate = st.text_input(label="insert partitionDate",value="*")

tab1, tab2 = st.tabs(["Horus", "Neogrid"])
col1, col2 = st.columns([3,15],gap="small")


with tab1:
    with st.container(height=200):
        fact,dim = st.tabs(["Fact","Dim"])
        with fact:
            
            horusItemSoldCkp = st.checkbox(label="horus:item_sold:trusted->parquet",value=False)
            horusFVendasEspandidoDeltaCkp = st.checkbox(label="horus:fVendas_expandido:refined->delta",value=False)
        with dim:
            horusProductCkp = st.checkbox(label="horus:product:trusted->parquet",value=False,key="horus_product")
            horusProductSegmentCkp = st.checkbox(label="horus:product_segment:trusted->parquet",value=False,key="product_segment")
            horusProductDeltaCkp = st.checkbox(label="horus:product:refined->delta",value=False)

tupleProcess += ((horusItemSoldCkp,tableItemSoldName,f"s3://obs-hwc-dev-dataplatform-trusted/horus/catalog/item_sold/dt={partitionDate}/*.parquet","parquet",10000,"obs"),)
tupleProcess += ((horusProductCkp,tableProductName,f"s3://obs-hwc-dev-dataplatform-trusted/horus/catalog/product/dt={partitionDate}/*.parquet","parquet",-1,"obs"),)
tupleProcess += ((horusProductSegmentCkp,tableProductSegment,f"s3://obs-hwc-dev-dataplatform-trusted/horus/catalog/product_segment/dt={partitionDate}/*.parquet","parquet",-1,"obs"),)
tupleProcess += ((horusProductDeltaCkp,tableProductDelta,f"s3://obs-hwc-dev-dataplatform-refined/performance_mercado/dproduto","delta",-1,"obs"),)
tupleProcess += ((horusFVendasEspandidoDeltaCkp,tableFVendasEspandidoDelta,"s3://obs-hwc-dev-dataplatform-refined/performance_mercado/fVendas_expandido","delta",-1,"obs"),)



# for ckbox in listTableInstances:
#     st.write(ckbox)
#     st.checkbox(label=f"{ckbox.sourceCompany}    {ckbox.schema} {ckbox.tableName}"
#                 ,value=False
#                 ,on_change=tableFlagChange(ckbox)
#                 )




with col1:
    if st.button("Create Table"):
        for tupla in tupleProcess:
            if tupla[0]:
                st.write(tupla)
                st.write(tupla[1])
                createOrDropTable(checkFlag=tupla[0],tableName=tupla[1],url=tupla[2],docType=tupla[3],limit=tupla[4],uri=tupla[5])
                
with col2:
    if st.button("Drop unchecked table"):
        for tupla in tupleProcess:
            if not tupla[0]:
                st.write(tupla)
                st.write(tupla[1])
                createOrDropTable(checkFlag=tupla[0],tableName=tupla[1],url=tupla[2],docType=tupla[3],limit=tupla[4],uri=tupla[5])
                
if st.button("Create From internal file"):
    listTableInstances = loadTablesInstances()
    loadTables(listTableInstances)

with st.expander("Upload tables conf:") :
    uploaded_file  = st.file_uploader("Choose a file",type="json",accept_multiple_files=False)
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)
        # To read file as string:
        string_data = stringio.read()
        listTableInstances = loadTablesInstances(string_data) 
        st.write(listTableInstances)
        loadTables(listTableInstances)

