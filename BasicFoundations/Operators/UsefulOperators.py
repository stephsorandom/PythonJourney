from typing import Iterable


Different Operators in Python

Range function:
mylist = [1,2,3]

for num in range(0,10,2):
    print(num)
    ##this will return numbers from 0 to 10, and even
    0 2 4 6 8

for num in range(0,10):
    print(num)
    0 1 2 3 4 5 6 7 8 9     ##similar to slicing



Enumerate function: 
 •Can take any Iterable object and returns an index counter and the object/element at that iteration.

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count =+ 1
    ===>
    At index 0 the letter a
     b
    At index 2 the letter c
    At index 3 the letter d
    At index 4 the letter e

This shows the letter at which index it is located. Such a simple but highly used function. There is an easier way 

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
    a
    b
    c
    d
    e

word = 'abcde'

for item in enumerate(word):
    print(item)
    ##returns the index_count in the form of Tuples!
    (0,'a')
    (1,'b')
    (2,'c')
    (3,'d')
    (4,'e')



Zip function: 
    • Opposotie of Enumerate. Zips together 2 list.

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)
    ##returns a list of tuples
    (1, 'a')
    (2, 'b')
    (3, 'c')


**  Zip will only return the list of tuples as much as it is able to....if you have multiple list and they do not have an equal number of items in each list, Zip will only return however many the smallest list of items **


In Operator:

'x' in [1,2,3] =====> False...x is not in the list

2 in [1,2,3] ======> True...2 is in the list


##in dictionaries

'mykey' in {'mykey':345}
    ===> True

d = {'mykey': 345}
345 in d.keys()    =====> False..345 is a value not a key

345 in d.values() =====> True...345 is a value!



Min & Max function:

mylist = [10,20,30,40,100]
min(mylist) ====> 10

max(mylist)   ======> 100


Random Library:
    • Python has a built in library, and Random is one of them. Similar to react and importing what functions you need to use!


from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
==>
[3,9,7,8,10,5,1,2,6,4]  ##every time you run shuffle, just keeps changing the order

##Grabing random integer
from random import randint
randint(0,100) ====> 79
                        **  randint returns a random integer each time  **
                        **  set parameters LO and HI so it can choose a number inbetween those  **



Accepting User Input: 

result = input('Enter a number here: ')
    this will prompt the user to enter desired information and you can save that input to a variable, and use that variable later in a function. 

    EX:
    result = input('What is your name?')

        User enters: 'Jose'



        later you call result and it returns 'Jose'

 • input() ===> Always accepts everything as a STRING....if they put a number in, it will return as a string. 
                Important when you are using that input data to get information.
                