Q1='''
    SELECT 
        *
    FROM
        ACTOR
    WHERE
        ID IN (
            SELECT 
                pid
            FROM
                Cast
                INNER JOIN Movie ON id=mid 
            WHERE name LIKE 'Annie%'
            );
    '''

Q2='''
    SELECT
        id,name,rank,year
    FROM
       Movie
    WHERE 
        year IN(1999,1994,2003) AND
        ID IN (
                SELECT 
                    mid
                FROM
                    MovieDirector
                    INNER JOIN Director ON id=did
                WHERE
                    fname ="Biff" AND lname="Malibu"
            
        
            )
    ORDER BY
        rank DESC,year;
    '''

Q3='''
    SELECT 
        year,COUNT(id) AS no_of_movies
    FROM
        Movie AS m
    GROUP BY 
        year
    HAVING
        AVG(rank)>(SELECT AVG(rank) FROM Movie)
    ORDER BY
        year;
    '''

Q4='''
    SELECT
        *
    FROM
        Movie
    WHERE 
        year=2001 AND
        rank < (SELECT AVG(rank) FROM Movie where year=2001)
    ORDER BY
        rank DESC
    LIMIT 10;
    '''
    
# Q5='''
#     SELECT 
#         id,
#         (SELECT 
#             COUNT(gender)
#         FROM
#             Actor INNER JOIN Cast ON id=pid
#         WHERE `Movie`.id=mid and gender='F'
#         ) AS no_of_female_actors,
#         (SELECT 
#             COUNT(gender) 
#         FROM
#             Actor INNER JOIN Cast ON id=pid
#         WHERE `Movie`.id=mid and gender='M'
#         ) AS no_of_male_actors
#     FROM
#         Movie
#     ORDER BY
#         id asc
#     LIMIT 
#         100;
#     '''

Q5='''
    SELECT
        movie_id,no_of_female_actors,no_of_male_actors 
    FROM
        (
            SELECT 
                COUNT(gender) AS no_of_male_actors,mid,md.id AS movie_id 
            FROM
                actor 
                INNER JOIN cast ON `actor`.id=pid 
                INNER JOIN movie AS md ON md.id=mid 
            WHERE gender='M' 
            GROUP BY md.id) Males INNER JOIN
        (
            SELECT
                count(gender) AS no_of_female_actors,mid
            FROM 
                actor 
                INNER JOIN cast ON `actor`.id=pid 
                INNER JOIN movie AS fd ON fd.id=mid 
            WHERE gender='F' 
            GROUP BY fd.id) Females ON Males.mid=Females.mid 
    LIMIT 10; 
'''

Q6='''
    SELECT 
        DISTINCT pid
    FROM
        Cast AS C
    WHERE EXISTS
        (SELECT pid FROM Cast WHERE pid=C.pid AND mid=C.mid GROUP BY pid HAVING COUNT(DISTINCT role)>1)
    ORDER BY
        pid ASC
    LIMIT 100;
    '''
     
Q7='''
    SELECT 
        fname,COUNT(fname) AS count
    FROM
        Director
    GROUP BY
        fname
    HAVING
        COUNT(fname)>1;
    '''

Q8='''
    SELECT 
       *
    FROM
        Director
    WHERE EXISTS 
        (
            SELECT 
                `Cast`.mid 
            FROM 
                Cast
                INNER JOIN MovieDirector ON `MovieDirector`.mid=`Cast`.mid
            WHERE `Director`.id=`MovieDirector`.did
            GROUP BY `MovieDirector`.mid
            HAVING COUNT(DISTINCT pid)>=100)
   AND NOT EXISTS 
        (
            SELECT 
                `Cast`.mid  
            FROM 
                Cast
                INNER JOIN MovieDirector ON `MovieDirector`.mid=`Cast`.mid
            WHERE `Director`.id=`MovieDirector`.did
            GROUP BY `MovieDirector`.mid
            HAVING COUNT(DISTINCT pid)<100);
    '''
