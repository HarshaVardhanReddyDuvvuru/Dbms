class InvalidField(Exception):
    pass

class Student:
    def __init__(self,student_id=None,name=None, age=None, score=None):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
            
    @classmethod
    def avg(cls,field, **kwargs):
        return cls.aggregator('AVG',field, **kwargs)
    
    @classmethod
    def min(cls,field, **kwargs):
        return cls.aggregator('MIN',field, **kwargs)
        
    @classmethod
    def max(cls,field, **kwargs):
        return cls.aggregator('MAX',field, **kwargs)
    
    @classmethod
    def count(cls,field=None,**kwargs):
        return cls.aggregator('COUNT',field,**kwargs)
        
    @classmethod
    def sum(cls,field, **kwargs):
        return cls.aggregator('SUM',field, **kwargs)
    
    @classmethod
    def aggregator(cls,aggregation,field, **kwargs):
        columns=[*cls().__dict__.keys()]
        if field==None and aggregation=='COUNT':
            field=columns[0]
        if field not in columns:
            raise InvalidField
        if len(kwargs)==0:
            sql_query = 'select {}({}) from student'.format(aggregation,field)
        else:
            multiple_conditions=[]
            for key,value in kwargs.items():
                parameters=key.split('__')
                operation_dict={"lt":'<',"gt":'>',"lte":'<=',"gte":'>=',"neq":'!=',"in":'in'}
                if parameters[0] not in columns:
                    raise InvalidField
                if len(parameters)==1:
                    if parameters[0] in columns:
                        condition='''{}="{}"'''.format(key,value)
                elif parameters[1]=="contains":
                    if not isinstance(value,str):
                        raise ValueError
                    condition='''name like "%{}%"'''.format(value)
                elif parameters[1]=="in":
                    if len(value)==1:
                        condition='''{} = {}'''.format(parameters[0],value[0])
                    else:
                        condition='''{} in {}'''.format(parameters[0],tuple(value))
                else:
                    if not isinstance(value,int):
                        raise ValueError
                    condition='''{} {} {}'''.format(parameters[0],operation_dict[parameters[1]],value)
                multiple_conditions.append(condition)
                
            multiple_conditions=' AND '.join(multiple_conditions)
            sql_query = 'select {}({}) from student where {}'.format(aggregation,field,multiple_conditions)
        ans=read_data(sql_query)
        return ans[0][0] 
            
def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans