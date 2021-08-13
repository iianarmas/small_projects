import mysql.connector
import time

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='s_projects')

cursor = db.cursor()

select = 'SELECT questions, answers FROM mini_quiz'

cursor.execute(select)

fetch = cursor.fetchall()

correct = 0
incorrect = 0

print(f'You must get a rate of 75% to pass\nGanbatte!')

for i in range(cursor.rowcount):
    time.sleep(1)
    print(f'\nQuestion #{i + 1}: {fetch[i][0]}')
    answer = input('Answer: ').strip().lower()
    if answer == fetch[i][1].lower():
        correct += 1
        time.sleep(0.5)
        print('Correct!')
        time.sleep(1)
    else:
        incorrect += 1
        time.sleep(0.5)
        print(f'Incorrect!\nCorrect Answer: {fetch[i][1]}')
        time.sleep(1)

rate = round((correct / cursor.rowcount) * 100, 2)

if rate >= 75:
    time.sleep(0.5)
    print(f'\nTotal Number of Questions: {cursor.rowcount}')
    time.sleep(0.4)
    print(f'Correct Answer: {correct}')
    time.sleep(0.3)
    print(f'Mistakes: {incorrect}')
    time.sleep(0.2)
    print(f'Rate: {rate}%')
    time.sleep(0.1)
    print('Congratulations!!')
else:
    time.sleep(0.5)
    print(f'\nTotal Number of Questions: {cursor.rowcount}')
    time.sleep(0.4)
    print(f'Correct Answer: {correct}')
    time.sleep(0.3)
    print(f'Mistakes: {incorrect}')
    time.sleep(0.2)
    print(f'Rate: {rate}%')
    time.sleep(0.1)
    print('That\'s okay! Try again next time okay?')
