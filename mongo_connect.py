from pymongo import MongoClient

def mongo_connect():
    driver = MongoClient()

    quiz_database = driver.get_database('D4E15')

    return quiz_database.get_collection('quizzes')
