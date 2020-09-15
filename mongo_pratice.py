import pymysql

driver = pymysql.connect(
    host='localhost',
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = driver.cursor()

cursor.execute('SELECT * FROM `d4e15`.`quiz`')
quizzes = cursor.fetchall()

for quiz in quizzes:
    cursor.execute(f'SELECT * FROM `d4e15`.`choice` WHERE quiz_id = {quiz["id"]}')
    choices = cursor.fetchall()
    if len(choices) != 0:
        print(quiz['question'])
        for i in range(len(choices)):
            print(f'{i+1}.{choices[i]['content']}')

        user_choice = int(input('enter your guest')) - 1
        if user_choice == quiz['awnser']:
            print('uh')
        else:
            print('nahhh')
