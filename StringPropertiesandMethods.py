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