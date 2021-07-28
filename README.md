# PythonJourney
Rules for Variable Names in Python : 
1. Can not start with a number. 
2. No spaces allowed in variable names. If you need more than one word, use Underscore _
3. No special characters :"'/?|()!@#$%^&~-+r
4. Best practice = keep Variable Name in lowercase.
5. Do not use data types as names : 'list' or 'str'


Python uses Dynamic Tying :  you can reassign a variable to different data types. 
    ->this increases functionality and run time, but gives chances of bug to occur due to possible different data types
    ex: my_dogs = 2 
        my_dogs = ['Sammy', 'Frankie']


- type() -> A function that shoes what data type is called 
    ex: a = 5           --> an integer 
        type(a) => int