## Shuffle a list with Random in python
cats = [1,2,3,4,5,6,7]

from random import shuffle 
shuffle(cats)

cats =>>> [5,3,2,7,4,1]


##Lets create our simple Three Cupe Monte game
def shuffle_list(mylist):   # Creating a function and parameter
    shuffle(mylist)  #  we will shuffle the parameter 'mylist'
    return mylist   #  and we will also return 'mylist'

    result = shuffle_list(cats)

    result ===>> [6,3,5,1,4,2,7]

#insert game 
## ' ' => empty cup 
## 'O' => cup with red ball in it
### shuffle the ball in the cup around and users must guess which cup it is in
mylist = [' ', 'O', ' ']

shuffle_list(mylist) ===>
                [ 'O', ' ',' ']
   


##Guessing location of ball in cup
def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
     guess = input("Pick a number: 0, 1, or 2")


    return int(guess)

myindex = player_guess() ===> 2 or whatever randomly generates


def check_guess(mylist, guess):
    if mylist[guess] == 'O':        ##if user chooses correct placement for ball 
        print('Correct!')           ##They are correct!
    else: 
        print('Wrong guess!')   ##If wrong answer is guessed, will return this string
        print(mylist)       ##Will also tell user where the ball actually was


#INITIAL LIST
mylist = [' ', 'O', ' ']

#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)


#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list, guess)