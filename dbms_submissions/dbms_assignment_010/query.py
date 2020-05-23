Q1='''
    SELECT 
        Player.player_id,MatchCaptain.team_id,jersey_no,name,date_of_birth,age
    FROM 
        MatchCaptain 
        INNER JOIN Player ON captain = Player.player_id
        LEFT JOIN GoalDetails ON captain=GoalDetails.player_id 
    WHERE
        Goal_id is null;
    
    '''
    
Q2='''
    SELECT
        Team_id,COUNT(match_no)
    FROM
        MatchTeamDetails
    GROUP BY 
        team_id;
    '''
    
Q3='''
    SELECT 
        Team_id,
        (
        SELECT
            COUNT(Goal_id)
        FROM
            GoalDetails
        WHERE 
            GoalDetails.Team_id=Team.Team_id
        )*1.0/
        (SELECT
            COUNT(player_id)
        FROM
            Player 
        WHERE Player.Team_id=Team.Team_id    
        ) as avg_goal_score
    FROM 
        Team
    WHERE
        avg_goal_score>0;
    '''
    
Q4='''
    SELECT
        captain,
        COUNT(captain) as no_of_times_captain
    FROM
        MatchCaptain
    GROUP BY
        captain;
    '''

Q5='''
    SELECT
        COUNT(DISTINCT captain) as no_players
    FROM
        MatchCaptain
        INNER JOIN Match on match.match_no=matchcaptain.match_no
        WHERE captain=player_of_match;
    '''    
        
Q6='''
    SELECT 
        DISTINCT(captain)
    FROM
        MatchCaptain
    WHERE NOT EXISTS(
                    SELECT
                        player_of_match 
                    FROM
                        Match
                    WHERE 
                        captain=player_of_match
                    );
    '''
    

Q7='''
    SELECT
        strftime('%m',play_date) AS month
        ,COUNT(match_no) 
    FROM 
        Match
    GROUP BY 
        month 
    ORDER BY
        COUNT(match_no) DESC;
    '''
    

Q8='''
    SELECT 
        jersey_no,COUNT(captain) AS no_captains
    FROM
        Player INNER JOIN MatchCaptain ON player_id=captain
    GROUP BY 
        jersey_no
    ORDER BY 
        no_captains DESC,
        jersey_no DESC;
    '''
    
Q9='''
    SELECT
        player_id ,AVG(audience) AS avg_audience
    FROM
        Match INNER JOIN MatchTeamDetails ON Match.match_no=MatchTeamDetails.match_no
        INNER JOIN Player ON MatchTeamDetails.Team_id=Player.Team_id
    GROUP BY 
        player_id
    ORDER BY
        avg_audience DESC,player_id DESC;
    '''

Q10='''
    SELECT
        Team_id,AVG(age)
    FROM 
        Player
    GROUP BY Team_id;
    
    '''

Q11='''
    SELECT
        AVG(age)
    FROM
        MatchCaptain INNER JOIN Player ON player_id=captain;
    '''

Q12='''
    SELECT
        strftime('%m',date_of_birth) as month,
        COUNT(player_id) as no_of_players
    FROM
        Player
    GROUP BY
        month
    ORDER BY
        no_of_players DESC,month DESC;
    '''

Q13='''
    SELECT
        captain,COUNT(win_lose)
    FROM
        MatchCaptain
        INNER JOIN MatchTeamDetails ON (
                            MatchCaptain.match_no=MatchTeamDetails.match_no AND
                            MatchCaptain.Team_id=MatchTeamDetails.Team_id
                            )
    WHERE
        win_lose="W"
    GROUP BY
        captain
    ORDER BY
        COUNT(win_lose) DESC;
    '''
        







# Q13='''
#     SELECT 
#         (SELECT 
#             captain
#         FROM 
#             MatchCaptain
#         WHERE
#             MatchCaptain.Team_id=MatchTeamDetails.Team_id
#         ) as captain,
#         COUNT(win_lose) as no_of_wins
#     FROM
#         MatchTeamDetails
#     WHERE
#         win_lose="W"
#     GROUP BY 
#         team_id
#     ORDER BY
#         COUNT(win_lose) DESC;
#     '''
    


  
  
    
    
    
    
    #     Team
    # GROUP BY 
    #     Team_id
    # HAVING
    #     (
    #     SELECT
    #         COUNT(Goal_id)
    #     FROM
    #         GoalDetails
    #     WHERE 
    #         GoalDetails.Team_id=Team.Team_id
    #     )>0