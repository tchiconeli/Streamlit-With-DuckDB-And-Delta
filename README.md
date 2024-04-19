# Streamlit-With-DuckDB-And-Delta
"Developed for data exploration using DuckDB as the SQL engine and compatible with Delta Table for data reading."

# Requirements
- Python 3.10

# Start venv
```
#cmd 
python -m venv venv
\venv\Scripts\activate
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
```


# TroubleShoting
If the query returns a memory error, it can be executed in two ways:
- Use comand 'Limit x' in the return of the data
- Set memory when start aplication (example: 5gb)
- ``` streamlit run main.py --server.maxMessageSize 5120 ```
