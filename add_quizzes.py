import pymysql

driver = pymysql.connect(
    host='localhost',
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = driver.cursor()

quiz_model = {
    'question': '',
    'choices': [],
    'awnser': 0
}
question = input('question: ')
choices = input('choices: ').split(',')
awnser = input('awnser: ')

quiz_model['question'] = question
quiz_model['awnser'] = int(awnser) - 1
quiz_model['choices'] = choices

print(quiz_model)

cursor.execute(f'''
    INSERT INTO `d4e15`.`quiz`(question, awnser)
    VALUES ('{quiz_model["question"]}', {quiz_model['awnser']})
''')

cursor.execute(f'''
    SELECT * FROM `d4e15`.`quiz` WHERE question = '{quiz_model["question"]}'
''')
new_quiz = cursor.fetchone()
for choice in choices:
    cursor.execute(f'''
        INSERT INTO `d4e15`.`choice`(content, quiz_id)
        VALUES ('{choice}', {new_quiz["id"]})
    ''')

driver.commit()
print('inserted question')

