from _typeshed import HasFileno


For Loops allow you to iterate through a block of code. 

    •Syntax of a for loop
        my_numbers = [1,2,3]  ##variable with list 
        for item_name in my_numbers: ##item_name represents the number in the my_numbers list 
            print(item_name)


    EX1:
    mylist = [1,2,3,4,5,6,7,8,9,10]
    ##create for loop to iterate through each item in the list
    for num in mylist: 
        print(num) 
            => 
            1
            2
            3
            4....prints every number individually 


    ## print only even numbers  
    for num in mylist:
        if num % 2 == 0: ##if the number divides by 2 and remander is 0, then it is even
            print(num)
                        ==>> 2,4,6,8,10

    ## print even and specific if odd
    for num in mylist:
        if num % 2 == 0:
            print(num)
        else: 
            print(f'Odd Number: {num}')   ## ----> f string literal?
                        ===> Odd Number: 1
                             2
                             Odd Number: 3
                             4.....and so on


    EX2:
    ##iterate through each number in list and add together
    list_sum = 0 

    for num in mylist: 
        list_sum = list_sum + num   ##list starts at 0 and adds each number 
        ##0 + 1+2+3+4+5+6+7+8+9+10
    print(list_sum) ====> 55


    EX3:
    mystring = 'Hello World'

    for letter in mystring:
        print(letter)
        ==> H
            e   
            l
            l.....o world 

    EX4: TUPLES AND FORLOOP
    tup = (1,2,3)

    for item in tup:
        print(item)
        ====> 1 2 3 

    mylist = [(1,2), (3,4), (5,6), (7,8)]  ##a list of tuples
    len(mylist) ==> 4     ##there are 4 items in this list

    for item in mylist: 
        print(item)   ==>
        (1,2)
        (3,4)
        (5,6)
        (7,8)

    EX5: Tuple unpacking
    mylist = [(1,2), (3,4), (5,6), (7,8)

    for(a, b) in mylist: 
        print(a)
        print(b) 
        ##this will unpack each tuple and print individually

    1
    2
    3
    4
    5....so on 
            ##you can also print each first number. 
        print(a)
        1,3,5,7
            ##or print the second number only. 
        print(b)
        2,4,6,8,10

    EX6: Tuples and unpacking at a larger scale
    mylist = [(1,2,3), (5,6,7), (8,9,10)]

    for item in mylist:
        print(item)             ===> prints each tuple group
        (1,2,3)
        (5,6,7)
        (8,9,10)


    mylist = [(1,2,3), (5,6,7), (8,9,10)]

    for item in mylist:
         