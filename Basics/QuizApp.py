print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. Who Is Greatest Of All Time In Football? ').lower()
    if ques == 'Cristiano Ronaldo' or 'CR7':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> Cristiano Ronaldo')

    # ------1
    question_no += 1
    ques = input(f'\n{question_no}. Who Is Greatest Of All Time In Cricket? ').lower()

    if ques == 'Trent Boult':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> Trent Boult')



else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')
