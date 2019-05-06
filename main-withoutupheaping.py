

import heapTuple


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
    #i=3
    #TestCase
    print("data")
    print("Number of balls",testVars[i][0])
    print("Max allowed turns",testVars[i][1])
    print("values on the balls",testVars[i][2])
    print("result of the coint toss",testVars[i][3])
    person = 0
    if testVars[i][3] == 'TAILS':
        person = 1

    print("1 = rusty, 0 = Scott")
    print("person: ",person)
    print("-----------------------------------------------------------------------------------------")

    #Setup data structures
    tupheap = heapTuple.BinaryHeap()
    for j in range(len(testVars[i][2])):
        sumVal = 0
        for k in range(len(testVars[i][2][j])):
            sumVal += int(testVars[i][2][j][k])
        tupheap.insert((int(testVars[i][2][j]), sumVal),person)

    print("initial dataset")
    print(tupheap.items)
    print("-----------------------------------------------------------------------------------------")

    playerSum = [0,0]
    #while there are still balls on the table
    while(len(tupheap)>0):
        #loop through players turns
        for z in range(testVars[i][1]):
            if z+1 == testVars[i][1]:
                toSeewhatHappening = tupheap.delete_min(1 - person)
            else:
                toSeewhatHappening = tupheap.delete_min(person)
            print("Choice:",toSeewhatHappening)
            #toSeewhatHappening = tupheap.delete_min(person)
            #print(toSeewhatHappening)
            playerSum[person] += toSeewhatHappening[0]
        print("end turn for",person)
        print()
        person = 1-person
        print("start turn for",person)

    print(playerSum)
    results.append(playerSum)

    #TestCase
    #break
    #TestCase
print("final",results)




#finds a prioritylist for rusty
#summedResults =[]







"""
somehow take the largest if there are multiple
error handling for delete_min
implement peek at min -> peek to see if the next number is the same
"""
