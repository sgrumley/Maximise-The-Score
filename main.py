import time
import heapTuple

#needs cleaning # break code into less options and verify before calling
def checkMax(pickedValue, heap):
    max = 0
    listofRustyChoice=[]
    listofRustyChoice.append(pickedValue)
    #Create a list of options for Rusty (same summed values) (Max 6 iterations on this dataset)
    while(heap.peek()[1] == listofRustyChoice[0][1]):
        listofRustyChoice.append(heap.removeMax(1))
        if len(heap)== 0:
            break
    #find the best choice for rusty based on the actual value
    for j in range(len(listofRustyChoice)):
        if listofRustyChoice[j][0] > listofRustyChoice[j][max]:
            max = j
    #any values not used got back into the list
    for j in range(len(listofRustyChoice)):
        if j != max:
            heap.insert(listofRustyChoice[j],1)
    return listofRustyChoice[max], heap

def readFile():
    file = open("input.txt", "r")
    i = 0
    testVars = []
    for line in file:
        if i == 0:
            numTests = int(line.split()[0])
            print("Total test cases:",numTests)
        elif i == 1:
            placehold = line.split()
            n,k = int(placehold[0]),int(placehold[1])
        elif i == 2:
            data = line.split()
        elif i == 3:
            gofirst = line.split()[0]
            temp =[]
            temp.append(n)
            temp.append(k)
            temp.append(data)
            temp.append(gofirst)
            testVars.append(temp)
            i=0
        i+=1
    return testVars, numTests

def dataStructure(ballVals,person):
    tupheap = heapTuple.PriorityQueue()
    for j in range(len(ballVals)):
        sumVal = 0
        for k in range(len(ballVals[j])):
            sumVal += int(ballVals[j][k])
        tupheap.insert((int(ballVals[j]), sumVal),person)
    return tupheap

def printArguments(testVars):
    print()
    print()
    print("-----------------------------------------------------------------------------------------")
    print("Number of balls on the table: ",testVars[0])
    print("Max turns allowed:",testVars[1])
    print("Result of the coint toss:",testVars[3])
    person = 0
    if testVars[3] == 'TAILS':
        person = 1
    print("1 = rusty, 0 = Scott")
    print("person: ",person)
    return person


def algorithm(testVars, testCaseNum):
    print("Test Case:", testCaseNum)
    #Declare variables with more readable names
    person = printArguments(testVars)
    maxTurns = testVars[1]
    numBalls = testVars[0]
    ballVals = testVars[2]
    flipResult = testVars[3]
    tupheap = dataStructure(ballVals,person)
    playerSum = [0,0]
    startTime=time.perf_counter()

    #while there are still balls on the table
    while(len(tupheap)>0):
        tupheap.heapify(person)
        #loop through players turns
        for z in range(maxTurns):
            pickedValue = tupheap.removeMax(person)
            #if the next value has the same summed value as current return the highest value
            try:
                if person == 1 and tupheap.peek()[1] == pickedValue[1]:
                    pickedValue, tupheap = checkMax(pickedValue, tupheap)
            except:
                pass
            #Sum the players choice to their total score
            playerSum[person] += pickedValue[0]
        #switch turns
        person = 1-person

    print()
    print("Time taken: ", time.perf_counter() - startTime)
    print("Sum of players:",playerSum)
    print("-----------------------------------------------------------------------------------------")
    return playerSum

""" Driver """
testVars, numTests = readFile()
#logic
#Iterate through all test cases
results=[]
for i in range(int(numTests)):
    results.append(algorithm(testVars[i],i+1))
#write out results
print("actua [[1000, 197], [240, 150], [2100000000, 98888899], [9538, 2256], [30031, 17796], [4726793900, 3941702128], [13793, 12543], [2173, 1665], [3923529875, 3049188235], [0, 284401]")
print("final",results)
