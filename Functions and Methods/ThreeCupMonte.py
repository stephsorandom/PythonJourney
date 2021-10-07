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
   
    