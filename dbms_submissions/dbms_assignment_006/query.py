Q1='''
    SELECT fname,lname
    FROM (Actor INNER JOIN cast on id=pid)
    WHERE mid=12148;
    '''
    
Q2='''
    SELECT COUNT(pid)
    FROM (Actor INNER JOIN cast ON id=pid)
    WHERE fname="Harrison (I)" AND lname="Ford";
    '''

Q3='''
    SELECT DISTINCT pid
    FROM (Movie INNER JOIN Cast ON id=mid)
    WHERE name LIKE 'Young Latin Girls%';
    '''
    
Q4='''
    SELECT COUNT(DISTINCT pid)
    FROM (Movie INNER JOIN Cast ON id=mid)
    WHERE year BETWEEN 1990 AND 2000;
    '''
    