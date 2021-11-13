import psycopg2

username = 'titomyr_labs'
password = '13579'
database = 'lab2'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

query_1 = '''
select country, count(country) as number_of_sportsmen from sportsman group by country
'''

query_2 = '''
select medal, count(medal) from sportsman_games
join sportsman on sportsman_games.sportsman_id = sportsman.sportsman_id group by medal
'''

query_3 = '''
select games_name, count(distinct(sportsman.sportsman_id)) from sportsman
join sportsman_games on sportsman.sportsman_id = sportsman_games.sportsman_id group by games_name
'''
cur = con.cursor()


def get_data(query):
    cur.execute(query_1)
    data = cur.fetchall()
    for el in data:
        print(el)
    return data


print('\n1.  \n')
data_1 = get_data(query_1)

print('\n2.  \n')
data_2 = get_data(query_2)

print('\n3.  \n')
data_3 = get_data(query_3)
