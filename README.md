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

# TroubleShoting
If the query returns a memory error, it can be executed in two ways:
- Use comand 'Limit x' in the return of the data
- Set memory when start aplication (example: 5gb)
- ``` streamlit run main.py --server.maxMessageSize 5120 ```
