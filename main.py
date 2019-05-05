
import heap


file = open("input.txt", "r")
i = 0
for line in file:
    print(line)
    if i == 0:
        numTests = line.split()[0]
    if i == 1:
        placehold = line.split()
        n,k = placehold[0],placehold[1]
    if i == 2:
        data = line.split()
    if i == 3:
        gofirst = line.split()[0]
    #call function to compute
    i+=1
file.close()

print(numTests, "tests total")
print("Number of balls",n,"Max allowed turns",k)
print("values on the balls",data)
print("result of the coint toss",gofirst)

#finds a prioritylist for rusty
summedResults =[]
for i in range(len(data)):
    sumVal = 0
    for j in range(len(data[i])):
        sumVal += int(data[i][j])
    summedResults.append(sumVal)
print("summed results",summedResults)

rustyBalls = heap.BinaryHeap()
rustyBalls.buildHeap(summedResults)
print(rustyBalls.items)


results = list(map(int, data))
scottBalls = heap.BinaryHeap()
scottBalls.buildHeap(results)
print(scottBalls.items)

scottSum = 0
rustySum = 0
"""
#have an array that is ordered by the first person?
if gofirst == "Tails":
    rustySum += balls.delete_min()
    #Rusty starts
else:
    scottSum += balls.delete_min()
    #Scott starts
print("Scott:", scottSum)
print("rusty", rustySum)
"""
