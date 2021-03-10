myUniqueList = []
myLeftOvers = []

def newlist(var):
    if var in myUniqueList:
        addtoleftovers(var)
        return False
    
    else: 
        myUniqueList.append(var)
        return True

def leftovers(var):
    myLeftOvers.append(var)
    

#My Homework #4 Test
print(myUniqueList)
print(newlist("80"))
print(newlist("85"))
print(newlist("80"))
print(myLeftOvers)