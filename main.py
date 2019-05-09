
import time
import heapTuple


# check this implementation does it check less options?
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



#needs cleaning # break code into less options and verify before calling
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

def readFile():
    print("ee")


file = open("input.txt", "r")
i = 0
testVars = []
for line in file:
    if i == 0:
        numTests = int(line.split()[0])
    if i == 4 or i == numTests-1:
        temp =[]
        temp.append(n)
        temp.append(k)
        temp.append(data)
        temp.append(gofirst)
        testVars.append(temp)
        i=1

    if i == 1:
        placehold = line.split()
        n,k = int(placehold[0]),int(placehold[1])
    if i == 2:
        data = line.split()
    if i == 3:
        gofirst = line.split()[0]
    i+=1

temp =[]
"""
print("rgkurgnkjsnfksjenfksjenfksefskejfskebfaljsbrflkjrflkb")
temp.append(n)
temp.append(k)
temp.append(data)
temp.append(gofirst)
testVars.append(temp)
"""
file.close()

print("Total test cases:",numTests)

results=[]
#Iterate through all test cases
for i in range(int(numTests)):
    #Declare variables with more readable names
    maxTurns = testVars[i][1]
    numBalls = testVars[i][0]
    ballVals = testVars[i][2]
    flipResult = testVars[i][3]

    #Print arguments for test case i
    print()
    print()
    print("Test Case:", i+1)
    print("-----------------------------------------------------------------------------------------")
    print("Number of balls on the table: ",testVars[i][0])
    print("Max turns allowed:",testVars[i][1])
    print("Result of the coint toss:",testVars[i][3])
    person = 0
    if flipResult == 'TAILS':
        person = 1
    print("1 = rusty, 0 = Scott")
    print("person: ",person)


    #Setup data structures
    tupheap = heapTuple.BinaryHeap()
    for j in range(len(ballVals)):
        sumVal = 0
        for k in range(len(ballVals[j])):
            sumVal += int(ballVals[j][k])
        tupheap.insert((int(ballVals[j]), sumVal),person)

    playerSum = [0,0]
    startTime=time.perf_counter()
    #while there are still balls on the table
    while(len(tupheap)>0):
        tupheap.buildHeap(person)
        #loop through players turns
        for z in range(maxTurns):
            #maybe pull pick then check peek and person 1 to determine whether check max should even be called
            if person == 1:
                toSeewhatHappening, tupheap = checkMax(tupheap)
            else:
                toSeewhatHappening = tupheap.delete_min(person)
            playerSum[person] += toSeewhatHappening[0]
        person = 1-person

    print()
    print("Time taken: ", time.perf_counter() - startTime)
    print("Sum of players:",playerSum)
    print("-----------------------------------------------------------------------------------------")
    results.append(playerSum)

print("actua [[1000, 197], [240, 150], [2100000000, 98888899], [9538, 2256], [30031, 17796], [4726793900, 3941702128], [13793, 12543], [2173, 1665], [3923529875, 3049188235], [0, 284401]")
print("final",results)
