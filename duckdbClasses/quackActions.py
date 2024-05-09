import duckdb
from deltaClasses import deltaActions
import os

class quackActions:
    
    def getConnection(dbName:str,readOnly:bool = False) -> duckdb.DuckDBPyConnection:
        if(dbName == ':default:'):
            return duckdb.connect(dbName)
        else:
            return duckdb.connect(f"databases/{dbName}.duckdb",read_only=readOnly)
        
        
    def setObsSecrets(connection:duckdb.DuckDBPyConnection):          
        connection.execute(f"""CREATE SECRET IF NOT EXISTS obs_dev (
            TYPE S3
            ,KEY_ID '{os.environ["ST_OBS_ACCESS_KEY_ID"]}'
            ,SECRET '{os.environ["ST_OBS_SECRET_ACCESS_KEY"]}'
            ,REGION 'LA-Santiago'
            ,ENDPOINT '{os.environ["ST_OBS_ENDPOINT"]}'
            ,use_ssl 0
        );""")
        
    def execQueryExistingTables(dbName:str,connection:duckdb.DuckDBPyConnection) :
        res = connection.sql("select table_catalog,table_schema,table_name from information_schema.tables").df()
        return res  
        
    def execQueryToPandasDF(q:str,connection:duckdb.DuckDBPyConnection):
        print("Executing query:")
        print(q)
        res = connection.sql(q).df()
        print("Execution query is done.")
        return res
    
    def execCreateTempTable(tableName:str, path:str, uri:str,schema:str,connection:duckdb.DuckDBPyConnection,docType,limit:int=100):
        print(path)
        cmd = f"""CREATE SCHEMA IF NOT EXISTS {schema};        
        CREATE TABLE IF NOT EXISTS {schema}.{tableName} AS
        SELECT * FROM """

        match docType:
            case "parquet":
                cmd = cmd + f"""read_parquet(['{path}'],filename=true)"""
            case "delta":
                res = deltaActions.getDeltatable(path,uri).to_pyarrow_table()             
                cmd = cmd + " res"
                limit = -1
            case other:
                print("DocType not found")

        if limit >= 0 :
            cmd = cmd+f" LIMIT {str(limit)}"
        print (f"executing: {cmd}")
        connection.execute(cmd)
        print (f"Exection query done")
            
        
    def execDropTempTable(tableName:str,connection:duckdb.DuckDBPyConnection):
        cmd = f"""DROP TABLE IF EXISTS {tableName}"""
        print (f"executing: {cmd}")
        connection.execute(f"""{cmd}""")