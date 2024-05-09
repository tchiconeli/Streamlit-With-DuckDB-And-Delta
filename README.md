# Streamlit-With-DuckDB-And-Delta
"Developed for data exploration using DuckDB as the SQL engine and compatible with Delta Table for data reading."

# Requirements
- Python 3.10

# Start venv
```
#powershell 
python -m venv venv
.\venv\Scripts\activate
```
# Install libs
```
#cmd 
pip install -r .\requirements.txt
```

# Start streamlit comand
```
# cmd
streamlit run main.py 
```

# Initialize the aplication with enviroment variables already set.

Now we can use enviroment variables in our aplication. In the aplication running we can set the values, but it's possible start the aplication with they already set.
Before start the aplication you can create them in the terminal. Follow the example
``` 
powershell 
$env:ST_OBS_ACCESS_KEY_ID='aaaaaa'
$env:ST_OBS_SECRET_ACCESS_KEY='aaaaaaaaa'
$env:ST_OBS_ENDPOINT_URL='https://obs.x.myhuaweicloud.com'
$env:ST_OBS_ENDPOINT='obs.x.myhuaweicloud.com'
$env:ST_OBS_REGION='x'
$env:ST_GCP_CREDENTIAL_PATH='c:\.....'
```
# Parameters that are accepet in the json for table load
- "sourceCompany": String - optional - Will be used for some feature in the feature - Default value set will be 'Personal';
- "tableName": String - required - Name of the table that will be created on duckdb
- "docType": String  - required - map the type of read that will be executed (for now, only works with parquet and delta);
- "schema": String  - optional - Determines the schema of table. Default value: 'main'
- "uri": String - required - Determines the source uri of the data. Values we work now:
    - "obs" - from huawei cloud storage;
    - "gs" - from google storage (for now, only work with Delta Table);
- "url": String - required - path for read the data; 
    - For parquet files will need to put all path with file name or using match parttern like 'path/*.parquet' to read all parquet in the folder;
    - For delta table, put the path for until the '_delta_logs';
- "limitDataframe": integer - optional - Determine a limit for the dataframe for insert that in the table. Default value: no limit;


# TroubleShoting
If the query returns a memory error, it can be executed in two ways:
- Use comand 'Limit x' in the return of the data
- Set memory when start aplication (example: 5gb)
- ``` streamlit run main.py --server.maxMessageSize 5120 ```
