

import heapTuple

def heapify(arr, n, i,person):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i][person] < arr[l][person]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest][person] < arr[r][person]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest,person)



#needs cleaning
def checkMax(heap):
    listofRustyChoice=[]
    listofRustyChoice.append(heap.delete_min(1))
    if len(heap)== 0:
        return listofRustyChoice[0], heap
    #Create a list of options for Rusty (same summed values)
    while(heap.peek()[1] == listofRustyChoice[0][1]):
        #print("--------------------()()()")
        listofRustyChoice.append(heap.delete_min(1))
        if len(heap)== 0:
            break
    if len(listofRustyChoice) == 1:
        return listofRustyChoice[0], heap
    max = 0
    #find the best choice for rusty based on the actual value
    for j in range(len(listofRustyChoice)):
        if listofRustyChoice[j][0] > listofRustyChoice[j][max]:
            max = j
    #any values not used got back into the list
    for j in range(len(listofRustyChoice)):
        if j != max:
            #print("getting inserted",listofRustyChoice[j])
            heap.insert(listofRustyChoice[j],1)
    return listofRustyChoice[max], heap

file = open("input.txt", "r")
i = 0
testVars = []
for line in file:
    if i == 4:
        temp =[]
        temp.append(n)
        temp.append(k)
        temp.append(data)
        temp.append(gofirst)
        testVars.append(temp)
        i=1
    if i == 0:
        numTests = line.split()[0]
    if i == 1:
        placehold = line.split()
        n,k = int(placehold[0]),int(placehold[1])
    if i == 2:
        data = line.split()
    if i == 3:
        gofirst = line.split()[0]

    #call function to compute
    i+=1
temp =[]
temp.append(n)
temp.append(k)
temp.append(data)
temp.append(gofirst)
testVars.append(temp)
file.close()

print(numTests, "tests total")
print(len(testVars))
results=[]
for i in range(int(numTests)):
    #TestCase
    #i=4
    #TestCase
    maxTurns = testVars[i][1]
    numBalls = testVars[i][0]
    ballVals = testVars[i][2]
    flipResult = testVars[i][3]
    print("data")
    print("Number of balls",testVars[i][0])
    print("Max allowed turns",testVars[i][1])
    print("values on the balls",testVars[i][2])
    print("result of the coint toss",testVars[i][3])
    person = 0
    if flipResult == 'TAILS':
        person = 1

    print("1 = rusty, 0 = Scott")
    print("person: ",person)
    print("-----------------------------------------------------------------------------------------")

    #Setup data structures
    tupheap = heapTuple.BinaryHeap()
    for j in range(len(ballVals)):
        sumVal = 0
        for k in range(len(ballVals[j])):
            sumVal += int(ballVals[j][k])
        tupheap.insert((int(ballVals[j]), sumVal),person)

    print("initial dataset")
    print(tupheap.items)
    print("-----------------------------------------------------------------------------------------")

    playerSum = [0,0]
    #while there are still balls on the table
    while(len(tupheap)>0):

        n = len(tupheap)
        for i in range(n, 0, -1):
            heapify(tupheap.items, n, i,person)

        tupheap.upHeap(person)
        tupheap.downHeap(1,person)

        #loop through players turns
        for z in range(maxTurns):
            #print(tupheap.items)
            if person == 1:
                toSeewhatHappening, tupheap = checkMax(tupheap)
            else:
                toSeewhatHappening = tupheap.delete_min(person)
            #print("chosen:",toSeewhatHappening)
            playerSum[person] += toSeewhatHappening[0]
        #print("end turn for",person)
        #print()
        person = 1-person
        #print("start turn for",person)

    print(playerSum)
    results.append(playerSum)

    #TestCase
    #break
    #TestCase

#print("git c [[1000, 197], [240, 150], [2100000000, 98888899], [9538, 2256], [31012, 16815], [4726793900, 3941702128], [13669, 12667], [2157, 1681], [4285558378, 2687159732], [0, 284401]]")
print("actua [[1000, 197], [240, 150], [2100000000, 98888899], [9538, 2256], [30031, 17796], [4726793900, 3941702128], [13793, 12543], [2173, 1665], [3923529875, 3049188235], [0, 284401]")
print("final",results)

#finds a prioritylist for rusty
#summedResults =[]







"""
somehow take the largest if there are multiple
error handling for delete_min
implement peek at min -> peek to see if the next number is the same
"""
