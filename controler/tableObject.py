

class tableForDuckdb:
    
    def __init__(self,sourceCompany, tableName, docType=None, schema=None, uri=None, url=None,flag=False):
        self.sourceCompany = sourceCompany
        self.tableName = tableName
        self.docType = docType
        self.schema = schema
        self.uri = uri
        self.url = url
        self.flag = flag
        
    def __str__(self):
        return f"Loader[tableName={self.tableName}, docType={self.docType}, schema={self.schema}, uri={self.uri}, url={self.url}]"