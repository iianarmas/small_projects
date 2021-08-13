import mysql.connector
import random

# to add some effect
from time import *
from datetime import datetime


# database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='s_projects')

cursor = db.cursor()

cursor.execute('SELECT questions, answers FROM mini_quiz')

fetch = cursor.fetchall()

# shuffle questions fetched from db
random.shuffle(fetch)

correct = 0
mistakes = 0
questions_num = 0


def qna():
    global correct, mistakes
    print(f'\nQuestion #{i + 1}: {fetch[i][0]}')
    answer = input('Answer: ').strip().lower()
    if answer == fetch[i][1].lower():
        correct += 1
        print('Correct!')
        sleep(1)
    else:
        mistakes += 1
        print(f'Incorrect!\nCorrect Answer: {fetch[i][1]}')
        sleep(1)


# user prompt
print(f'Total Questions as of {datetime.now()}, is: {cursor.rowcount}')
user = input('Enter the number of questions you wish to answer (Type "all" if you want to answer all): ')
print(f'\nYou must get a rate of 75% to pass\nGod bless!')

# check number of questions to answer
if user == 'all':
    for i in range(cursor.rowcount):
        qna()
        questions_num += 1
else:
    for i in range(int(user)):
        qna()
        questions_num += 1

rate = round((correct / questions_num) * 100, 2)

if rate >= 75:
    sleep(0.5)
    print(f'\nTotal Number of Questions: {questions_num}')
    sleep(0.4)
    print(f'Correct Answer: {correct}')
    sleep(0.3)
    print(f'Mistakes: {mistakes}')
    sleep(0.2)
    print(f'Rate: {rate}%')
    sleep(0.1)
    print('Congratulations!!')
else:
    sleep(0.5)
    print(f'\nTotal Number of Questions: {questions_num}')
    sleep(0.4)
    print(f'Correct Answer: {correct}')
    sleep(0.3)
    print(f'Mistakes: {mistakes}')
    sleep(0.2)
    print(f'Rate: {rate}%')
    sleep(0.1)
    print('That\'s okay! Try again next time okay?')
