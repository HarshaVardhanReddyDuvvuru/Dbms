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
#             field,operator=key.split('__')
#             value=value
#         if field not in ["student_id","age","name","score"]:
#             raise InvalidField
#         if operator=="gt":
#             sql_query='select * from Student where {}>{}'.format(key,value)
#         if operator=="lt":
#             sql_query='select * from Student where {}<{}'.format(key,value)
#         ans=read_data(sql_query)
#         if len(ans)==0:
#             raise DoesNotExist
#         if len(ans)>1:
#             raise MultipleObjectsReturned
            
#         object=cls(ans[0][1],ans[0][2],ans[0][3])
#         object.student_id=ans[0][0]
#         return object

#     def delete(self):
#         write_data('DELETE FROM student WHERE student_id={}'.format(self.student_id)) 
        
#     def save(self):
#         import sqlite3
#         connection = sqlite3.connect("students.sqlite3")
#         crsr = connection.cursor()
#         crsr.execute("PRAGMA foreign_keys=on;")
#         if self.student_id==None:
#             sql_query='''INSERT INTO Student(name,age,score)
#                             values(?,?,?)
#                         '''
#             values=(self.name,self.age,self.score)
#             crsr.execute(sql_query,values)
#             self.student_id=crsr.lastrowid
            
#         if self.student_id!=None:
#             sql_query='''UPDATE Student SET 
#                             name=?,
#                             age=?,
#                             score=?
#                             WHERE student_id=?
#                             '''
#             values=(self.name,self.age,self.score,self.student_id)
#             crsr.execute(sql_query,values)

        
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

# student_object = Student.get(student_id__gt=1)


