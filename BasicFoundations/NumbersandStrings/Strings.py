from types import SimpleNamespace


String Rules: 
1. 'hello'
2. "hello"
3. "I don't know how to write Python" 
        -> In the 3rd example, you can wrap a string in double quotes ("") and use a single quote inside as punctuation.

Indexing & Slicing can be used in Python because strings are `ordered sequences`
    -> you can grab specific sections of the string by using bracket notation []
        -> Indexing starts at 0. 
            -> Reverse Indexing goes backwards. to find the end of the string simply use -1


Slicing allows you to grab a subsection of multiple characters by using the following: 
    -> [start:stop:step]
        -> start : where you start slice
        -> stop : where you want to stop (you go up to this number but do not include it)
        -> step : size of the "jump" you take from start to stop

To execute Python you must use print()

- using \n => creates a new line. 

print('Hey there my name is \n Stephanie!') 
    => Hey there my name is
        -> Stephanie!

- using \t => creates a tab space.

print('Hello \tWorld!')  => Hello    World!

- using len() => returns length of string

len('I am')  => 4