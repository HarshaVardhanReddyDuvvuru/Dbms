Q1='''
    SELECT
        AVG(age) 
    FROM
        Player;
    '''

Q2='''
    SELECT
        match_no,
        play_date
    FROM 
        match 
    WHERE
        audience>50000
    ORDER BY
        match_no ASC;
    '''

Q3='''
    SELECT
        team_id,
        count(match_no) AS [ the number of matches the team has won]
    FROM 
        matchteamdetails 
    WHERE
        win_lose='W' 
    GROUP BY 
        team_id
    HAVING 
        count(match_no)>=1 
    ORDER BY
        count(match_no) DESC ,
        team_id ASC;
    '''

Q4='''
    SELECT
        match_no,
        play_date
    FROM
        match
    WHERE
        stop1_sec > (
            SELECT 
                AVG(stop1_sec)
            FROM 
                match
            )
    ORDER BY
        match_no DESC,
        play_date DESC;
    '''

Q5='''SELECT
        match_no,
        team.name,
        player.name AS name
    FROM 
        matchcaptain
        INNER JOIN team ON matchcaptain.team_id=team.team_id 
        INNER JOIN player ON player_id=captain
    ORDER BY 
        match_no ASC,team.name ASC;
    '''
    
Q6='''SELECT
        match_no,name,
        jersey_no 
    FROM
        match 
        INNER JOIN player ON player_of_match=player_id
    ORDER BY 
        match_no ASC;
    '''

Q7='''
    SELECT
        team.name,
        AVG(age) AS average_age
    FROM
        team 
        INNER JOIN player ON team.team_id=player.team_id
    GROUP BY
        team.name 
    HAVING 
        AVG(age)>26
    ORDER BY
        team.name ASC,
        AVG(age) ASC;
    '''

Q8='''
    SELECT
        name,
        jersey_no,
        age,
        count(goal_id) AS [the number of goals scored] 
    FROM
        player 
        INNER JOIN goaldetails ON player.player_id=goaldetails.player_id
    WHERE
        age<=27
    GROUP BY
        name
    ORDER BY
        count(goal_id) DESC,
        name ASC;
    '''

Q9='''
    SELECT
        team_id,(
            SELECT
                count(goal_id)
            FROM goaldetails
            WHERE
                goaldetails.team_id=team.team_id)*100.0/(
            SELECT
                count(goal_id) 
            FROM goaldetails
            )  
        FROM 
            team 
        WHERE 
            (
            SELECT 
                count(goal_id) 
                FROM 
                    goaldetails 
                WHERE 
                    team.team_id=goaldetails.team_id)>0;
     '''

Q10='''
    SELECT
        AVG(goals)
    FROM (
        SELECT
            count(goal_id) AS goals
        FROM 
            goaldetails 
        GROUP BY
            team_id
        );
    '''

Q11='''
    SELECT
        player_id,name,date_of_birth 
    FROM 
        player 
    WHERE NOT EXISTS(
                    SELECT
                        goal_id
                    FROM
                        goaldetails 
                    WHERE 
                        player.player_id=goaldetails.player_id
                    )
        ORDER BY
            player_id ASC;
    '''


Q12='''
    SELECT
        name,match.match_no,
        match.audience,
        match.audience-(
                        SELECT 
                            AVG(match.audience)
                        FROM 
                            match
                            INNER JOIN matchteamdetails AS mtd ON mtd.match_no=match.match_no 
                        WHERE matchteamdetails.team_id=mtd.team_id)
    FROM
        matchteamdetails
        INNER JOIN match ON matchteamdetails.match_no=match.match_no 
        INNER JOIN team ON matchteamdetails.team_id=team.team_id
    ORDER BY 
        match.match_no;'''






# Q12='''SELECT (SELECT name FROM team WHERE team.team_id=mtd.team_id) AS name,mtd.match_no,(SELECT audience FROM match WHERE match.match_no=mtd.match_no) AS audience,
#   (SELECT audience FROM match WHERE match.match_no=mtd.match_no )-(SELECT AVG(audience) FROM match INNER JOIN matchteamdetails ON match.match_no=matchteamdetails.match_no WHERE matchteamdetails.team_id=mtd.team_id) AS diff     FROM matchteamdetails AS mtd ORDER BY mtd.match_no;
#     '''

