select country, count(country) as number_of_sportsmen from sportsman group by country

select medal, count(medal) from sportsman_games
join sportsman on sportsman_games.sportsman_id = sportsman.sportsman_id group by medal

select games_name, count(distinct(sportsman.sportsman_id)) from sportsman
join sportsman_games on sportsman.sportsman_id = sportsman_games.sportsman_id group by games_name