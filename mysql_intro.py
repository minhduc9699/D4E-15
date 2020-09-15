import pymysql

driver = pymysql.connect(
    host='localhost',
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = driver.cursor()

# cursor.execute('CREATE DATABASE d4e15')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS `d4e15`.`quiz`(
#     id int AUTO_INCREMENT,
#     question varchar(255),
#     awnser varchar(255),
#     PRIMARY KEY(id)
# )
# ''')

# cursor.execute(''' 
#     CREATE TABLE `d4e15`.`choice`(
#         id int AUTO_INCREMENT,
#         content varchar(255),
#         quiz_id int,
#         FOREIGN KEY(quiz_id) REFERENCES `quiz`(id),
#         PRIMARY KEY(id)
#     )
# ''')
