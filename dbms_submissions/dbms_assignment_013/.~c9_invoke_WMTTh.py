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
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        crsr = connection.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if self.student_id==None:
            crsr.execute('''INSERT INTO Student(name,age,score)
                            values(?,?,?)
                        ''',(self.name,self.age,self.score))
            self.student_id=crsr.lastrowid
            connection.commit()
            
        if self.student_id!=None:
            ans=read_data('''SELECT
                                *
                            FROM
                                Student
                            WHERE
                                student_id={}
                        '''.format(self.student_id))
                        
            if ans==[]:
                crsr.execute('''INSERT INTO
                                    Student
                                    values(?,?,?,?)
                            ''',(self.student_id,self.name,self.age,self.score))
                connection.commit()
            
            else:
                crsr.execute('''UPDATE Student SET 
                                name=?,
                                age=?,
                                score=?
                                WHERE student_id=?
                                ''',(self.name,self.age,self.score,self.student_id))
                connection.commit()
        connection.close()
    
    @classmethod
    def filter(cls,**kwargs):
        fields=[]
        field_values=[]
        for key,value in kwargs.items():
            if key not in ["student_id","name","age","score"]:
                raise InvalidField
            if key in ["student_id","name","age","score"]:
                fields.append(key)
                field_values.append(value)
                
            elif key in ["student_id_lt","age_lt","score_lt"]:
                field=
                sql_query='''select * from Student where {}<{}'''.format(key,value)
                
            elif key in ["student_id_lte","age_lte","score_lte"]:
                sql_query='''select * from Student where {}<={}'''.format(key,value)
                
            elif key in ["student_id_gt","age_gt","score_gt"]:
                sql_query='''select * from Student where {}>{}'''.format(key,value)
                
            elif key in ["student_id_gte","age_gte","score_gte"]:
                sql_query='''select * from Student where {}>={}'''.format(key,value)
                
            elif key in ["student_id_nqe","age_nqe","score_nqe","name_nqe"]:
                sql_query='''select * from Student where {}!={}'''.format(key,value)
                
            elif key in ["student_id_in","age_in","score_in","name_in"]:
                sql_query='''select * from Student where {} in {}'''.format(key,value)
            
            elif key in ["student_id_in","age_in","score_in"]:
                sql_query='''select * from Student where {} in {}'''.format(key,value)
                
            elif key in ["name_contains"]:
                sql_query='''select * from Student where name like %"{}"%'''.format(value)
            
        if len(fields)>0:
            if len(fields)==1:
                sql_query='''select * from Student where {}="{}"'''.format(fields[0],field_values[0])
                
            elif len(fields)==2:
                sql_query='''select * from Student where {}="{}" AND {}="{}"'''.format(fields[0],field_values[0],fields[1],field_values[1])
            
            elif len(fields)==3:
                sql_query='''select * from Student where {}="{}" AND {}="{} AND {}="{}"'''.format(fields[0],field_values[0],fields[1],field_values[1],fields[2],field_values[2])
            
            else:
                sql_query='''select * from Student where {}="{}" AND {}="{} AND {}="{}" AND {}="{}"'''.format(fields[0],field_values[0],fields[1],field_values[1],fields[2],field_values[2],fields[3],field_values[3])
          
        ans=read_data(sql_query)
        li=[]
        for i in range(len(ans)):
            object="Student(name={0}, age={1}, score={2})".format(
            ans[i][1],
            ans[i][2],
            ans[i][3])
            object.student_id=ans[i][0]
            li.append(object)
        
        return li
        
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	