class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    @classmethod
    def get(cls,**kwargs):
        for key,value in kwargs.items():
            if key not in ["student_id","name","age","score"]:
                raise InvalidField
            sql_query='select * from Student where {}="{}"'.format(key,value)
    
        ans=read_data(sql_query)
        if len(ans)>1:
            raise MultipleObjectsReturned
        if len(ans)==0:
            raise DoesNotExist
            
        object=cls(ans[0][1],ans[0][2],ans[0][3])
        object.student_id=ans[0][0]
        return object

    def delete(self):
        sql_query='DELETE FROM student WHERE student_id={}'.format(self.student_id)
        write_data(sql_query)
        
    def save(self):
        if self.student_id==None:
            sql_query="""INSERT INTO Student(name,age,score) values('{}',{},{})""".format(self.name,self.age,self.score)
            crsr=write_data(sql_query)
            self.student_id=crsr.lastrowid
            
        if self.student_id!=None:
            ans=read_data('''SELECT
                                *
                            FROM
                                Student
                            WHERE
                                student_id={}
                        '''.format(self.student_id))
            if ans==[]:
                sql_query="""INSERT INTO Student values({},'{}',{},{})""".format(self.student_id,self.name,self.age,self.score)
                write_data(sql_query)
            
            else:
                sql_query='''UPDATE Student SET 
                                name='{}',
                                age={},
                                score={}
                                WHERE student_id={}
                                '''.format(self.name,self.age,self.score,self.student_id)
                write_data(sql_query)
    
    @classmethod
    def filter(cls,**kwargs):
        ans=cls.sql_generator(**kwargs)
        objects_list=[]
        for i in range(len(ans)):
            object=Student(ans[i][1],ans[i][2],ans[i][3])
            object.student_id=ans[i][0]
            objects_list.append(object)
                
        return objects_list
    
    @classmethod
    def avg(cls,field, **kwargs):
        return cls.sql_generator('AVG',field, **kwargs)
    
    @classmethod
    def min(cls,field, **kwargs):
        return cls.sql_generator('MIN',field, **kwargs)
        
    @classmethod
    def max(cls,field, **kwargs):
        return cls.sql_generator('MAX',field, **kwargs)
    
    @classmethod
    def count(cls,field=None,**kwargs):
        return cls.sql_generator('COUNT',field,**kwargs)
        
    @classmethod
    def sum(cls,field, **kwargs):
        return cls.sql_generator('SUM',field, **kwargs)
    
    @staticmethod
    def sql_generator(aggregation=None,field=None,**kwargs):
        if len(kwargs)==0:
            if field==None and aggregation=='COUNT':
                field="student_id"
            if field not in ["student_id","name","age","score"]:
                raise InvalidField
            sql_query = 'select {}({}) from student'.format(aggregation,field)
            ans=read_data(sql_query)
            return ans[0][0] 
                
            
        else:
            multiple_conditions=[]
            for key,value in kwargs.items():
                parameters=key.split('__')
                operation_dict={"lt":'<',"gt":'>',"lte":'<=',"gte":'>=',"neq":'!=',"in":'in'}
                
                if parameters[0] not in ["student_id","name","age","score"]:
                    raise InvalidField
                    
                if len(parameters)==1:
                    if parameters[0] in ["student_id","name","age","score"]:
                        condition='''{}="{}"'''.format(key,value)
                
                elif parameters[1]=="contains":
                    condition='''name like "%{}%"'''.format(value)
                
                elif parameters[1]=="in":
                    p=tuple(value)
                    condition='''{} in {}'''.format(parameters[0],p)
    
                else:
                    condition='''{} {} {}'''.format(parameters[0],operation_dict[parameters[1]],value)
                multiple_conditions.append(condition)
                
            multiple_conditions=' AND '.join(multiple_conditions)
            
            if aggregation!=None:
                sql_query = 'select {}({}) from student where '.format(aggregation,field)+ multiple_conditions
                ans=read_data(sql_query)
                return ans[0][0] 
                
            else:
                sql_query = 'select * from student where '+ condition
                return read_data(sql_query)

            
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
	return crsr

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans











# class DoesNotExist(Exception):
#     pass

# class MultipleObjectsReturned(Exception):
#     pass

# class InvalidField(Exception):
#     pass

# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.student_id = None
#         self.age = age
#         self.score = score
    
#     @classmethod
#     def get(cls,**kwargs):
#         for key,value in kwargs.items():
#             if key not in ["student_id","name","age","score"]:
#                 raise InvalidField
#             sql_query='select * from Student where {}="{}"'.format(key,value)
    
#         ans=read_data(sql_query)
#         if len(ans)>1:
#             raise MultipleObjectsReturned
#         if len(ans)==0:
#             raise DoesNotExist
            
#         object=cls(ans[0][1],ans[0][2],ans[0][3])
#         object.student_id=ans[0][0]
#         return object

#     def delete(self):
#         sql_query='DELETE FROM student WHERE student_id={}'.format(self.student_id)
#         write_data(sql_query)
        
#     def save(self):
#         import sqlite3
#         connection = sqlite3.connect("students.sqlite3")
#         crsr = connection.cursor()
#         crsr.execute("PRAGMA foreign_keys=on;")
#         if self.student_id==None:
#             crsr.execute('''INSERT INTO Student(name,age,score)
#                             values(?,?,?)
#                         ''',(self.name,self.age,self.score))
#             self.student_id=crsr.lastrowid
#             connection.commit()
            
#         if self.student_id!=None:
#             ans=read_data('''SELECT
#                                 *
#                             FROM
#                                 Student
#                             WHERE
#                                 student_id={}
#                         '''.format(self.student_id))
#             if ans==[]:
#                 crsr.execute('''INSERT INTO
#                                     Student
#                                     values(?,?,?,?)
#                             ''',(self.student_id,self.name,self.age,self.score))
            
#             else:
#                 crsr.execute('''UPDATE Student SET 
#                                 name=?,
#                                 age=?,
#                                 score=?
#                                 WHERE student_id=?
#                                 ''',(self.name,self.age,self.score,self.student_id))
#         connection.commit()
#         connection.close()
        
# def write_data(sql_query):
# 	import sqlite3
# 	connection = sqlite3.connect("students.sqlite3")
# 	crsr = connection.cursor() 
# 	crsr.execute("PRAGMA foreign_keys=on;") 
# 	crsr.execute(sql_query) 
# 	connection.commit() 
# 	connection.close()

# def read_data(sql_query):
# 	import sqlite3
# 	connection = sqlite3.connect("students.sqlite3")
# 	crsr = connection.cursor() 
# 	crsr.execute(sql_query) 
# 	ans= crsr.fetchall()  
# 	connection.close() 
# 	return ans
	