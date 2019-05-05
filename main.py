
import heap
import heapTuple


file = open("input.txt", "r")
i = 0
for line in file:
    """
    print(line)
    if i == 0:
        numTests = line.split()[0]
    if i == 1:
        placehold = line.split()
        n,k = int(placehold[0]),int(placehold[1])
    if i == 2:
        data = line.split()
    if i == 3:
        gofirst = line.split()[0]
    """
    if i == 0:
        numTests = line.split()[0]
    if i == 10:
        placehold = line.split()
        n,k = int(placehold[0]),int(placehold[1])
    if i == 11:
        data = line.split()
    if i == 12:
        gofirst = line.split()[0]
    #call function to compute
    i+=1
file.close()

print(numTests, "tests total")
print("Number of balls",n,"Max allowed turns",k)
print("values on the balls",data)
print("result of the coint toss",gofirst)

tupheap = heapTuple.BinaryHeap()

#finds a prioritylist for rusty
#summedResults =[]
person = 0
if gofirst == 'TAILS':
    person = 1

print("1 = rusty, 0 = Scott")
print("person: ",person)

for i in range(len(data)):
    sumVal = 0
    for j in range(len(data[i])):
        sumVal += int(data[i][j])
    print(data[i], sumVal)
    tupheap.insert((int(data[i]), sumVal),person)

print("initial dataset",tupheap.items)
playerSum = [0,0]
while(len(tupheap)>0):
    for i in range(k):
        if len(tupheap)>0:
            #test
            if person == 1 and tupheap.delete_min(1)[1] == 13:
                print("whats the orderrerererr",tupheap.items)
            #pull all numbers until there is a difference take the biggest value and insert the rest
            #or when looking for the max compare values as well
            #test

            if i+1 == k:
                toSeewhatHappening = tupheap.delete_min(1 - person)[0]
            else:
                toSeewhatHappening = tupheap.delete_min(person)[0]
            print("Choice:",toSeewhatHappening)
            playerSum[person] += toSeewhatHappening
    person = 1-person
    print("change in turn",person)


print(playerSum)


"""
somehow take the largest if there are multiple
error handling for delete_min
"""
