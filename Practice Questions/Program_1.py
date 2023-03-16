# Get index in the list of objects by attribute in Python

class List:
    def __init__(self, val):
        self.val = val
    
def printListObjects(emptyListForStoringObjects, valueInIndex):
    for idx, val in enumerate(emptyListForStoringObjects):
        if(val.val == valueInIndex):
            return 'Found'
        
    

listContainerForObjects = [1, 2, 3, 4, 5]

emptyListForStoringObjects = list()

for i in listContainerForObjects:
    emptyListForStoringObjects.append(List(i))


print(printListObjects(emptyListForStoringObjects, 3))
