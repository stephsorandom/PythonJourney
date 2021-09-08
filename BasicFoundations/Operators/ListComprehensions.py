List Comprehensions 
    •List Comprehensions can be a unqiue way of quickly creating a list with python. Instead of using a For Loop and .append() to create a list....just use List Comprehension!

            Syntax:
            variable = element for element in 'desired word'

            Ex1:
                #declare variable
            mystring = 'hello'
                #For Looop to separate the string into a list of strings
            for letter in mystring:
                mylist.append(letter)
                #Call the variable 
                    mylist ====> ['h','e','l','l','o']

    LIST COMPREHENSIONS EX:
            mystring = 'hello'

            mylist = [leter for letter in mystring]
                    ## takes the ELEMENT for ELEMENT in another list...and appends it 

            ===> #Call the variable 
                mylist ====> ['h','e','l','l','o']

        EX2: 
            mylist = [x for x in range(0,11)]

            ===> [0,1,2,3,4,5,6,7,8,9,10,11]

                ## Now return results by even numbers only
            mylist = [x for x in range(0,11) if x % 2 == 0]

            ===> [0,2,4,6,8,10]

        EX3:
        celicus = [0,10,20,34.5]

        fahrenheit = [( (9/5)* temp + 32) for temp in celicus]

        fahrenheit ===> [32.0, 50.0, 68.0, 94.1]


        ORRRRRRR
        
        fahrenheit = []

        for temp in celcius: 
            fahrenheit.append((9/5) * temp + 32)


            ====>
        fahrenheit ===> [32.0, 50.0, 68.0, 94.1]


Nested Loops
    EX1:
    mylist = []

    for x in [2,4,6]: ##loop
        for y in [100,200,300]: ##within loop
            mylist.append(x*y) ##multiply each one
            ##Call variable
            mylist = [200,400,600, 400,800,1200, 600,1200,1800]

ORRRRRRR
    mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
    ##Call variable
            mylist = [200,400,600, 400,800,1200, 600,1200,1800]