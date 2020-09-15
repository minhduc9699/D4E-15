from mongo_connect import mongo_connect

quiz_collection = mongo_connect()

quizzes = quiz_collection.find()

for quiz in quizzes:
    print(quiz['question'])
    choices = quiz['choices']
    for i in range(len(choices)):
        print(f'{i+1}.{choices[i]}')

    user_choice = int(input('enter your guest')) - 1
    if user_choice == quiz['awnser']:
        print('uh')
    else:
        print('nahhh')
