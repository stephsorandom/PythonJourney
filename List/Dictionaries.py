Are unordered mappings for storing objects. 
You can grab an object in a list without having to know its index. You can just call the key associated with that value and retrieve it. 

Ex: {'key1':'value1', 'key2':'value2'}

Think about what you need and how you need it.....
                    Dictionaries vs Lists

    ~ Dictioniaries: Objets are retrieved by a key name. So you don't need to know the index position....but, Dictionaries can't be sorted!!

    ~ Lists: Objects are retrieved by locations (index). So you need more information to access it, more strict in a way. But you can index and sort and arrange the information in a more valuable way.

    Dictionary Examples : 

    prices_lookup = {'apple' : 2.99, 'oranges' : 1.99, 'milk': 5.80}
    #Now to use prices_lookup to call a value 
    prices_lookup['apple'] =====> 2.99

    Dictionaries can hold multiple types of values. Strings, integers, floating integers, other list, other dictionaries, 

    dict1 = {'k1':123, 'k2': [0,1,2], 'k3': {'insideKey':100}}
    # if you want to grab elements from this dictionary 
    d['k1'] => 123
    # or 
    d['k3'] => {'insideKey': 100}
    #if you just want to call the value, 100, and not the value AND key 
    d['k3']['insideKey'] ===> 100

    ## Preforming a toUpper Function!####

    d = {'key1': ['a', 'b', 'c']}
    d['key1'][2].upper()      =>    'C'


    #Add new value to dictionary
d = {'k1':100, 'k2': 200}
d['k3'] = 300 
d =>>>>>>>>>>> {'k1':100, 'k2': 200, 'k3': 300}

    #Assign new value to an existing key 
d = {'k1':100, 'k2': 200, 'k3': 300}
d['k1'] = 'NEW VALUE'
d = {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}

    #Check all keys in dictionary
d.keys() =>>> dict_keys(['k1', 'k2', 'k3'])

    #Check all values in dictionary
d.values() ====>>>>> dict_values([100,200,300])

    #Check all item pairings
d.items() ====>>> dict_items([('k1', 100), ('k2', 200), ('k3', 300)])

That is all for now folks!

