from pymongo import MongoClient
import pymysql

mongo_driver = MongoClient()
movie_database = mongo_driver.get_database('d4e12')
movie_collection = movie_database.get_collection('movies')

mysql_driver = pymysql.connect(
    host='localhost',
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = mysql_driver.cursor()
def movie_table():
    # EXTRACT
    source_movies = movie_collection.find({"year": {"$exists": True}})

    for movie in source_movies:
        # TRANSFORM 
        target_movie = {
            "name": movie["title"],
            "year": str(movie["year"])
        }
        # LOAD
        cursor.execute(f'''
            INSERT INTO 
            `d4e15`.`movie`(name, year)
            VALUES ('{target_movie["name"]}', '{target_movie["year"]}')
        ''')


# EXTRACT
source_actors = movie_collection.aggregate([
    {
        '$match': {
            'year': {'$exists': True}
        }
    },
    {
        '$unwind': '$actors'
    },
    {
        '$group': {
            '_id': '',
            'actors': {'$addToSet': '$actors'}
        }
    }
])

for actor in list(source_actors)[0]['actors']:
    # LOAD
    cursor.execute(f''' 
        INSERT INTO `d4e15`.`actor`(name)
        VALUES('{actor}')
    ''')



mysql_driver.commit()
