Sets are unordered collections of UNIQUE elements.

Ex: 
    myset = set()  ====> set()

    #Add to Set
    myset.add(1)  ====> {1}
    myset.add(2)  ====> {1, 2}
    #Add a duplicate to Set
    myset.add(2)  ====> {1, 2}     ###It simply does not add the duplicate to the Set


    #Casting a list to Set to get back unique value
    newlist = [1,1,2,3,3,3,3,3,3,3,,4,5,6]
    set(newlist)   =====> {1,2,3,4,5,6}
                        ~Helpful when you are looking for any unique values....remember they do not have any sort of Order to them...these values just happen to be in order from smallest to larget!