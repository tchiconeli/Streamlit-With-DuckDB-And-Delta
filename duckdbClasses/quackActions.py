import duckdb
from helpers import helpers
from deltaClasses import deltaActions

class quackActions:
        
    def setObsSecrets():
        data = helpers.loadObsConf()            
        duckdb.execute(f"""CREATE SECRET IF NOT EXISTS obs_dev (
            TYPE S3
            ,KEY_ID '{data["OBS_DEV"]["access_key_id"]}'
            ,SECRET '{data["OBS_DEV"]["secret_access_key"]}'
            ,REGION 'LA-Santiago'
            ,ENDPOINT '{data["OBS_DEV"]["endpoint"]}'
            ,use_ssl 0
        );""")
        
    def execQueryToPandasDF(q:str):
        res =""
        print(q)
        return duckdb.sql(q).df()
    
    def execCreateTempTable(tableName:str, path:str, uri:str,docType,limit:int=100):
        cmd = f"""CREATE TEMP TABLE IF NOT EXISTS {tableName} AS
                  SELECT * FROM """

        match docType:
            case "parquet":
                cmd = cmd + f"""read_parquet("{path}",filename=true)"""
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
            
        
    def execDropTempTable(tableName:str):
        cmd = f"""DROP TABLE IF EXISTS {tableName}"""
        print (f"executing: {cmd}")
        duckdb.execute(f"""{cmd}""")