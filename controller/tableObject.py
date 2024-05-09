

class tableForDuckdb:
    
    def __init__(self, tableName:str, docType:str=None, sourceCompany:str="Personal",schema:str='main', uri=None, url=None,flag=False,limitDataframe:int=-1):
        self.sourceCompany = sourceCompany
        self.tableName = tableName
        self.docType = docType
        self.schema = schema
        self.uri = uri
        self.url = url
        self.flag = flag
        self.limitDataframe = limitDataframe
        
    def __str__(self):
        return f"Loader[tableName={self.tableName}, docType={self.docType}, schema={self.schema}, uri={self.uri}, url={self.url}]"
