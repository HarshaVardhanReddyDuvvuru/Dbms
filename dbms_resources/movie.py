# class Movie:
#     def __init__(self,id=None,name=None,year=None,rank=None):
#         self.id=id
#         self.name=name
#         self.year=year
#         self.rank=rank

#     for key,value in kwargs.items():
#         parameters=key.split('__')
#         operation_dict={"lt":'<',"gt":'>',"lte":'<=',"gte":'>=',"neq":'!=',"in":'in'}
#             if parameters[0] not in columns:
#                     raise InvalidField
#                 if len(parameters)==1:
#                     if parameters[0] in columns:
#                         condition='''{}="{}"'''.format(key,value)
#                 elif parameters[1]=="contains":
#                     if not isinstance(value,str):
#                         raise ValueError
#                     condition='''name like "%{}%"'''.format(value)
#                 elif parameters[1]=="in":
#                     p=tuple(value)
#                     condition='''{} in {}'''.format(parameters[0],p)
#                 else:
#                     if not isinstance(value,int):
#                         raise ValueError
#                     condition='''{} {} {}'''.format(parameters[0],operation_dict[parameters[1]],value)
#                 multiple_conditions.append(condition)
                
#             multiple_conditions=' AND '.join(multiple_conditions)



# import sqlite3,random,string
# connection = sqlite3.connect("movie_booking_slots.sqlite3")
# crsr=connection.cursor()
# names=[]
# for i in range(20):
#     alphabets=list(string.ascii_lowercase)
#     name=''
#     for i in range(random.randint(1,20)):
#         name+=random.choice(alphabets)
#     names.append(name)

# for i in range(1000):
#     name=random.choice(names)
#     gender=random.choice(['M','F'])
#     age=random.randint(5,100)
#     movie_id=random.randint(1,100)
#     theater_id=random.randint(1,100)
#     crsr.execute('''INSERT INTO Audience(name,gender,age,movie_id,theater_id) values(?,?,?,?,?)''',(name,gender,age,movie_id,theater_id))
    
# connection.commit()
# connection.close()
def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("imdb.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

ans=read_data('''select distinct(name) from movie inner join cast on id=mid limit 10''')
for i in ans:
    print(i)

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
	return crsr