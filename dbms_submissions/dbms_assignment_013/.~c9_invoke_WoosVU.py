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
#     def __repr__(self):
#         return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
#             self.student_id,
#             self.name,
#             self.age,
#             self.score)
            
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
#         if self.student_id==None:
#             sql_query="""INSERT INTO Student(name,age,score) values('{}',{},{})""".format(self.name,self.age,self.score)
#             crsr=write_data(sql_query)
#             self.student_id=crsr.lastrowid
            
#         if self.student_id!=None:
#             ans=read_data('''SELECT
#                                 *
#                             FROM
#                                 Student
#                             WHERE
#                                 student_id={}
#                         '''.format(self.student_id))
#             if ans==[]:
#                 sql_query="""INSERT INTO Student values({},'{}',{},{})""".format(self.student_id,self.name,self.age,self.score)
#                 write_data(sql_query)
            
#             else:
#                 sql_query='''UPDATE Student SET 
#                                 name='{}',
#                                 age={},
#                                 score={}
#                                 WHERE student_id={}
#                                 '''.format(self.name,self.age,self.score,self.student_id)
#                 write_data(sql_query)
    
#     @classmethod
#     def filter(cls,**kwargs):
#         flag=0
#         multiple_condition_set=set()
#         for key,value in kwargs.items():
#             field=key.split('__')
#             operation_dict={"lt":'<',"gt":'>',"lte":'<=',"gte":'>=',"neq":'!=',"in":'in'}
            
#             if field[0] not in ["student_id","name","age","score"]:
#                 raise InvalidField
                
#             if len(field)==1:
#                 if field[0] in ["student_id","name","age","score"]:
#                     condition='''{}="{}"'''.format(key,value)
            
#             elif field[1]=="contains":
#                 condition='''name like "%{}%"'''.format(value)
            
#             elif field[1]=="in":
#                 if len(value)==1:
#                     condition='''{}={}'''.format(field[0],value[0])
#                 else:
#                     p=tuple(value)
#                     condition='''{} in {}'''.format(field[0],p)

#             else:
#                 condition='''{} {} "{}"'''.format(field[0],operation_dict[field[1]],value)
                
#             sql_query = 'select * from student where '+ condition
                
#             ans=read_data(sql_query)
#             objects_list=[]
#             strings_of_objects_list=[]
#             for i in range(len(ans)):
#                 object=Student(ans[i][1],ans[i][2],ans[i][3])
#                 object.student_id=ans[i][0]
#                 objects_list.append(object)
#                 strings_of_objects_list.append(str(object))
                
#             temp=set(strings_of_objects_list)
            
#             if flag==0: 
#                 multiple_condition_set=temp
#                 initial_object_list=objects_list
#                 flag=1
#             multiple_condition_set=temp&multiple_condition_set
            
#         all_objects=[]
#         for i in initial_object_list:
#             if str(i) in multiple_condition_set:
#                 all_objects.append(i)
                
#         return all_objects
        
            
# def write_data(sql_query):
# 	import sqlite3
# 	connection = sqlite3.connect("selected_students.sqlite3")
# 	crsr = connection.cursor() 
# 	crsr.execute("PRAGMA foreign_keys=on;") 
# 	crsr.execute(sql_query) 
# 	connection.commit() 
# 	connection.close()
# 	return crsr

# def read_data(sql_query):
# 	import sqlite3
# 	connection = sqlite3.connect("selected_students.sqlite3")
# 	crsr = connection.cursor() 
# 	crsr.execute(sql_query) 
# 	ans= crsr.fetchall()  
# 	connection.close() 
print(s)
	