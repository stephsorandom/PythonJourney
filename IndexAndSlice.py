 ~ Indexing
mystring = 'Hello World'
# we want to find the first character
mystring[0] => 'H'
mystring[7] => 'o'
mystring[-3] => 'r'
mystring[-1] => 'd'


~ Slicing
mystring = 'abcdefghijk'
#we want to slice from 'c' all the way to the end
mystring[2:] => 'cdefghijk'
#grab a, b, c
mystring[:3] => 'abc' #counts to index 3 'the letter D' but does not include it when returning
#grab d,e,f
mystring[3:6] => 'def'

#grab from the beginning to end of string 
mystring[::] => 'abcdefghijk'
#beginning to end, skip 2
mystring[::2] => 'acegik'
# by 3
mystring[::3] => 'adgj'

# jump by command start at 2, finish at 7, jump by 2
mystring[2:7:2] => 'ceg'

#reverse a string
mystring[::-1] => 'kjihgfedcba'