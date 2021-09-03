If, Elif, Else Statements

    ~ Control Flow Syntax in Python use of colons, indentation and whitespace 
        • This is VERY important and sets Python apart from other programming languages. 


    if some_condition : 
        # execute some code 

    else : 
        # do something else

    elif some_other_condition : 
        #do something different         
                elif ----> for a completely different condition..You can use as many elif statements


Ex1:
    if True: 
        print('ITS TRUE!')
    if 3 > 2: 
        print('Yes it is true')  -----> 'Yes it is true'


    hungry = True  ===> declaring variable
    if hungry: ====> arguement
        print('Feed me')  ====> what it prints if True
    else: 
        print('Im not hungry')

Ex2:
    loc = 'Bank'

    if loc == 'Auto Shop' :
        print('Cars are cool!')
    else: 
        print('I don not know much.')


Ex using elif: 

loc = 'Store'

    if loc == 'Auto Shop' :
        print('Cars are cool!')
    elif loc == 'Bank' :
        print('Money is cool!')
    elif loc == "Store" :
        print('Publix is cool!')
    else: 
        print('Where am I?')

            ===> 'Publix is cool!' ##because we declared loc = 'Store'



Ex: 

name = 'Steph'

    if name == 'Nat': 
        print('Hey Nat!')
    elif name == 'Steph':
        print('Whats up Steph!')
    else : 
        print('What is your name?')

        ====> "Whats up Steph!"