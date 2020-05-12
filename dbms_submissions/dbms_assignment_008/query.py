Q1='''select id,fname from director as d 
where not exists (select * from moviedirector as mv inner join movie on `movie`.id=`mv`.mid where d.id=mv.did and year<2000) and
exists (select * from moviedirector as md inner join movie on `movie`.id=`md`.mid  where d.id=md.did and year>2000) order by id asc;'''


Q3='''select * from actor as a 
    where not exists(select id from movie inner join cast on id=mid 
    where year between 1990 and 2000 and pid=a.id) order by id desc limit 100;'''
    
 
Q2='''select fname,
    (select name from movie inner join moviedirector on id=mid 
    where did=director.id order by rank desc,name limit 1)
    from director limit 100;'''
    