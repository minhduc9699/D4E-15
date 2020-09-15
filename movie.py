import pymysql

driver = pymysql.connect(
    host='localhost',
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = driver.cursor()

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS `d4e15`.`movie`(
        id int(11) AUTO_INCREMENT,
        name varchar(255),
        year varchar(255),
        PRIMARY KEY(id)
    )
''')

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS `d4e15`.`actor`(
        id int(11) AUTO_INCREMENT,
        name varchar(255),
        age varchar(255),
        PRIMARY KEY(id)
    )
''')

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS `d4e15`.`movie_actor`(
        movie_id int(11),
        actor_id int(11),
        FOREIGN KEY(movie_id) REFERENCES `movie`(id),
        FOREIGN KEY(actor_id) REFERENCES `actor`(id),
        PRIMARY KEY(movie_id, actor_id)
    )
''')
