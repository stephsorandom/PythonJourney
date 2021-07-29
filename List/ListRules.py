from typing_extensions import TypeAlias


List Rules: 
1. List are ordered sequences.
2. They use [] and commas ,  to separate objects in the list
            [1,2,3,4,5]
3.Can be nested and support the usage of indexing and slicing. 

EX:
    my_list = [1,2,3]    -> list of integers
    my_list = ['Hello', 50, 0.175]    -> list can use multiple data type
            len(my_list)  => 3
    my_list = ['one', 'two', 'three']
        #grab first index spot
        my_list[0]          => 'one'
        #start at index one and grab everything after
        my_list[1:]         => ['two', 'three']

You can also concatanate list, just like strings, but with a bit more freedom
    EX:  my_list = ['one', 'two', 'three']
         another_list = ['four', 'five']
         new_list = my_list + another_list          => ['one', 'two', 'three', 'four', 'five']

List allow you to change individual objects. 
#change index[0] to uppercase
    EX: new_list[0] = 'ONE'                          => ['ONE', 'two', 'three', 'four', 'five']


#add 'six' to the END of list 
.append()  -> allows you to add any item to the end of a list 

new_list.append('six')                               => ['ONE', 'two', 'three', 'four', 'five', 'six']

#removes item from the END of a list
.pop() -> removes an item from the end of a list 

new_list.pop('six')                                  => ['ONE', 'two', 'three', 'four', 'five']

.pop() -> also allows indexing to remove from specific spot on list

new_list.pop(0)                                      => ['two', 'three', 'four', 'five']


.sort() -> sorts in alphabetical or acsending numerical order
    #no argument passes through .sort()......paraenthasis are left blank  

    EX: letter_list = ['a', 'd', 'e', 'c', 'b']
        num_list = [6,3,2,4,5,1]
        letter_list.sort()                      => ['a', 'b', 'c', 'd', 'e']
        num_list.sort()                         => [1,2,3,4,5,6]


.reverse() -> reverses list
    #no argument passes through .reverse()

    EX: num_list.reverse()                      => [6,5,4,3,2,1]