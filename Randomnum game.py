import random 

random_num = int(random.random() *  100)
print("Guess the number ")
game_state ='undone'
score = 0

while game_state == 'undone' :
    guess_num_by_user = int(input())
    if(guess_num_by_user == random_num):
        print('correct!!!')
        score += 1
        print('Your score: ', int(score))
        random_num = int(random.random() * 100)
    elif(guess_num_by_user < random_num):
        print('More!')
    elif(guess_num_by_user > random_num):
        print('Less!')
