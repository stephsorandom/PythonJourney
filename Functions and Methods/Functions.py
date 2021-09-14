def Keyword: 
    stands for the definition of the function
            def name_of_function():
                '''
                Docstring explains the function with 3 Quotes. 
                Everything inside the function is indented

                '''
                - Python uses snake casing in functions..all lowercase with underscores_between_words

        EX:
        def name_of_function(name):
            '''
            print("Hello" + name)
            )
            '''

    name_of_function("Jose")
    ---> Hello Jose

    • Return keyword

        - Typically 'return' is used to send back the results of the function instead of just printing it out. 
        - 'Return' allows us to assign the ouput of the function to a new variable.
        
        EX:
            def add_function(num1 + num2)
            return num1 + num2    ##Return allows to save the result to a variable!

            result = add_function(1,2)
            ## 1 + 2 ===> 3
            print(result)           ====>>> 3 

    
        EX2:
        def say_hello(name):
            print(f'Hello {name}')

            say_hello(Jose) ======>> Hello Jose

        def say_hello(name='Default'):
            print(f'Hello {name}')

            say_hello() =====>> Hello Default


• The difference between print and result
    PRINT

    def print_result(a,b):
        print(a+b)

    result = print_result(10,20)
    ====> 30
            ## print_result is not actually saving any part of the function.
            ## it is just executing the function and then closing it right after.
            ## If you call result again later...it will return nothing. becaues it is a instant command
    type(result) ====> NoneType


    RESULT  

    def return_result(a,b):
        return a+b

    result = return_result(10,20)

##call the function later in your code
    result ====>>> 30





Functions with Logic: 

def even_check(number):
    number % 2 == 0 
    return result 

    even_check(20)
        ==> True
    even_check(21)
        ==> False

        ## True or False if any even number in List
def check_even_list(num_list):      #num_list gets passed into function to be executed

    for number in num_list:     ##loops through all numbers in list 
        if number % 2 == 0:     ##if any number is Modulos to 2...or even, 
            return True         ##return true
        else:                   ## else skip that number and continue looping
            pass

    return False               ## if there are no even numbers in the whole Loop...then return false



## Now return all even numbers in a list, if no even numbers..return empty list

def check_even(num_list):
even_numbers = []           ##placeholder 

for number in num_list:     ##loops through the list in the function argument
    if number % 2 == 0:     ## if the number is even 
        even_numbers.append(number)     ## append =>> add to even_number list

    else:
        pass

return even_numbers     ##return the even_number list
