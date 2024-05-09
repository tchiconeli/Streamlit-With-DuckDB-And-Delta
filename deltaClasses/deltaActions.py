from deltalake import DeltaTable
from helpers import helpers
import os


def getStorageOptionsObs():
    access_key = os.environ["ST_OBS_ACCESS_KEY_ID"]
    secret = os.environ["ST_OBS_SECRET_ACCESS_KEY"]
    endpoint_url= os.environ["ST_OBS_ENDPOINT_URL"]
    region = os.environ["ST_OBS_ENDPOINT"]
    storage_options = {
            "access_key_id":f"{access_key}",
            "secret_access_key":f"{secret}",
            "endpoint_url": f"{endpoint_url}",
            "AWS_S3_ALLOW_UNSAFE_RENAME":"true",    
            "region": f"{region}"
            }
    return storage_options

def getStorageOptionsGCP():
    return {"GOOGLE_SERVICE_ACCOUNT_PATH": f'{os.environ["ST_GCP_CREDENTIAL_PATH"]}' }


def getDeltatable(path, uri):
    st:dict = {}
    match uri:
        case "obs":
            st = getStorageOptionsObs()           
        case "gs":
            st = getStorageOptionsGCP()
        case other:
            "Error: uri not found"
    return DeltaTable(path,storage_options=st)
        
def getDeltaFilesURIPath(path, uri):
    return getDeltatable(path,uri).file_uris()