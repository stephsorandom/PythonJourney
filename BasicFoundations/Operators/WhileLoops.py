While Loops: 
    • While loops continue to execute a block of code WHILE some conditions remains TRUE.

        SYNTAX: 
            while some_boolean_condition:
                #do something
            else: 
                #do something different

    EX1:
    x = 0
    while x < 5:
        print(f'The current value of x is {x}')
        x = x + 1 
        ##b x += 1 ##same as writing it like above
        ==>
        The current value of x is 0
        The current value of x is 1
        The current value of x is 2
        The current value of x is 3
        The current value of x is 4
        ## stops at 4, because if x = 5....5 is not < 5
    


    EX2: include an ELSE 
    while x < 5:
            print(f'The current value of x is {x}')
            x += 1
    else: 
        print('X IS NOT LESS THAN 5') 
        ===>
        The current value of x is 0
        The current value of x is 1
        The current value of x is 2
        The current value of x is 3
        The current value of x is 4
        X IS NOT LESS THAN 5




Break, Continue, Pass
    • We can use break, continue, and pass statements in our loops to add additional functionality for various cases. 


        •break: Breaks out of the current closest enclosing loop.
        •continue: Goes to the top of the closest enclosing loop.
        •pass: Does nothing at all.

    EX1: pass

    x = [1,2,3]
    
    for item in x:
        pass    ##----> pass is used as a placeholder, when you want nothing done. If you do not include pass, you get a syntax error. 
    print('end of my script')
        ====> end of my script



    EX2: continue

    mystring = 'Sammy'

    for letter in mystring: 
        print(letter)
        S
        a
        m
        m
        y

## lets say you don't want to print out the letter A
    for letter in mystring:
        if letter == 'a':
            continue    ##once it finds the letter 'a', the loop will continue without it
        print(letter)
        S
        m
        m
        y


    EX3: break

    mystring = 'Sammy'

    for letter in mystring:
        if letter == 'a':
            break   ##once it finds the letter 'a', the loop will break before it. 
        print(letter)
        S


    EX4: break with a while statement

    x = 0

    while x < 5:
        print(x)
        x += 1
        ====>
        0 1 2 3 4

    while x < 5:

        if x ==2:
            break
        print(x)
        x += 1
        ===>
        0 1  ##once the condition gets to 2. breaks before it 