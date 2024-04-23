import duckdb
from deltaClasses import deltaActions
import os

class quackActions:
        
    def setObsSecrets():          
        duckdb.execute(f"""CREATE SECRET IF NOT EXISTS obs_dev (
            TYPE S3
            ,KEY_ID '{os.environ["ST_OBS_ACCESS_KEY_ID"]}'
            ,SECRET '{os.environ["ST_OBS_SECRET_ACCESS_KEY"]}'
            ,REGION 'LA-Santiago'
            ,ENDPOINT '{os.environ["ST_OBS_ENDPOINT"]}'
            ,use_ssl 0
        );""")
        
    def execQueryExistingTables() :
        return duckdb.sql("select table_catalog,table_schema,table_name from information_schema.tables").df()    
        
    def execQueryToPandasDF(q:str):
        res =""
        print(q)
        return duckdb.sql(q).df()
    
    def execCreateTempTable(tableName:str, path:str, uri:str,docType,limit:int=100):
        cmd = f"""CREATE TEMP TABLE IF NOT EXISTS {tableName} AS
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
        duckdb.execute(cmd)
        print (f"Exection query done")
            
        
    def execDropTempTable(tableName:str):
        cmd = f"""DROP TABLE IF EXISTS {tableName}"""
        print (f"executing: {cmd}")
        duckdb.execute(f"""{cmd}""")