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
Caso a query retorne erro de memoria, pode ser executado de duas formas:
- Limitar o dataframe retornado
- Setar a memoria no inicio da execução (exemlo de 5gb)
- ``` streamlit run main.py --server.maxMessageSize 5120 ```