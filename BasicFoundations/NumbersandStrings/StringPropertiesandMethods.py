-Immutability = You can not change once declared

    Strings are Immutable. You can not use Indexing to change individual characters in a string 
    
    ex: name = 'Sam'

        #You can't just reassign index positions. 
        name[0] ='P' ----------------> NOOOOO
        #if you want to change Sam to Pam, you must concatanate 
        last_letters = name[1:]
            -> last_letters => 'am'
            "P" + last_letters 
                -> 'Pam'

            Ex: 
        x = 'Hello World'
        x = x + ' it is beautiful outside!'
        x =>> 'Hello World it is beautiful outside!'

        letter = 'z'
        letter * 5 = 'zzzzz'

        letter.upper() => ZZZZZ
        letter.lower() => zzzzz
        letter.split() => ['z','z', 'z', 'z', 'z', 'z']



- String Interpolation 

.format() method: Allows you to insert into a print statment by using object format
    EX: print('This is a string {}'.format('INSERTED'))  
                => 'This is a string INSERTED'

You can use index positioning with .format to insert in any desired order 
    EX1: print('The {2} {1} {3}'.format('fox', 'brown', 'quick'))
                => 'The quick brown fox'
    EX2: print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
                => 'The quick brown fox'



- Float Formatting

Allows you to adjust the width and precision of floating point number
                print('The result {}'.format(value:width.precision f))

- F strings (Formatted String Literals)

Allows you to skip the .format() and write the variable directly inside the string.
    EX1: name = 'Jose'
        print(f'Hello, his name is {name}') 
                        => 'Hello, his name is Jose'   =========>> New to Python 3.0!!