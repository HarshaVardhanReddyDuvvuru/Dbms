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
            
            else:
                crsr.execute('''UPDATE Student SET 
                                name=?,
                                age=?,
                                score=?
                                WHERE student_id=?
                                ''',(self.name,self.age,self.score,self.student_id))
        connection.commit()
        connection.close()
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	