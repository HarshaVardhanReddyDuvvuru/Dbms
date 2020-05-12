Q1='''
    SELECT COUNT(*)
    FROM movie
    WHERE year<2000;
    '''
    
Q2='''
    SELECT AVG(rank)
    FROM movie
    WHERE year=1991;
    '''
    
Q3='''
    SELECT MIN(rank)
    FROM movie
    WHERE year=1991;
    '''

Q4='''
    SELECT fname,lname
    FROM Actor INNER JOIN Cast ON id=pid
    WHERE mid=27;'''
    
Q5='''
    SELECT COUNT(mid)
    FROM Actor INNER JOIN Cast ON id=pid
    WHERE fname="Jon" AND lname="Dough";
    '''
    
Q6='''
    SELECT name AS names
    FROM movie 
    WHERE name LIKE 'Young Latin Girls%' AND year BETWEEN 2003 AND 2006;
    '''

Q7='''
    SELECT fname,lname
    FROM (movie INNER JOIN movieDirector on movie.id=movieDirector.mid)
    INNER JOIN Director on movieDirector.did=director.id
    WHERE movie.name LIKE 'Star Trek%';
    '''

Q8='''
    select name from movie 
    inner join moviedirector on `movie`.id=`movieDirector`.mid  
    inner join cast on `cast`.mid=`movie`.id 
    inner join actor on `cast`.pid=`actor`.id
    inner join director on `director`.id='movieDirector'.did
    where `actor`.fname='Jackie (I)' and `actor`.lname='Chan' and `director`.fname='Jackie (I)' and `director`.lname='Chan' ORDER BY name Asc; 
    '''

Q9='''
    SELECT fname,lname
    FROM (director INNER JOIN movieDirector on id=did) as details
    INNER JOIN movie on details.mid=movie.id 
    WHERE year=2001
    GROUP BY fname,lname
    HAVING COUNT(fname)>=4
    ORDER BY fname ASC, lname DESC;
    '''


Q10='''
    SELECT gender,count(*)
    FROM Actor 
    GROUP BY gender
    ORDER BY gender ASC;
    '''

Q11='''
    select a.name,b.name,a.rank,a.year 
    from movie as a cross join movie as b 
    where a.year=b.year and a.rank=b.rank and a.name!=b.name
    order by a.name asc
    limit 100;
    '''


Q12='''
    SELECT fname, year,avg(rank) as rank 
    from(actor inner join cast on id=pid) as details inner join movie on movie.id=details.mid 
    group by actor.id,year
    order by fname asc,year DESC limit 100;
    '''
    
Q13='''
    SELECT actor.fname,director.fname,avg(rank) as score from director
    inner join moviedirector on `director`.id=`movieDirector`.did
    inner join movie on `movie`.id=`movieDirector`.mid
    inner join cast on `cast`.mid=`movie`.id 
    inner join actor on `cast`.pid=`actor`.id
    group by actor.id,director.id
    HAVING COUNT(*)>=5
    order by score DESC,director.fname ASC,actor.fname DESC limit 100;
    '''
    
