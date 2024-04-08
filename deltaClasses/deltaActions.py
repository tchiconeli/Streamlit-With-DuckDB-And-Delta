from deltalake import DeltaTable
from helpers import helpers
import polars


def getStorageOptionsObs():
    data = helpers.loadObsConf()
    access_key = data["OBS_DEV"]["access_key_id"]
    secret = data["OBS_DEV"]["secret_access_key"]
    endpoint_url= data["OBS_DEV"]["endpoint_url"]
    region = data["OBS_DEV"]["region"]
    storage_options = {
            "access_key_id":f"{access_key}",
            "secret_access_key":f"{secret}",
            "endpoint_url": f"{endpoint_url}",
            "AWS_S3_ALLOW_UNSAFE_RENAME":"true",    
            "region": f"{region}"
            }
    return storage_options

def getDeltatable(path, uri):
    match uri:
        case "obs":
            return DeltaTable(path,storage_options=getStorageOptionsObs())
        case other:
            "Error"
        
