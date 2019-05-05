class BinaryHeap(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    #parent node = node position / 2
    def upHeap(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, item):
        self.items.append(item)
        self.upHeap()

    #
    def downHeap(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i] < self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2] > self.items[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def delete_min(self):
        return_value = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.downHeap(1)
        return return_value

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.items = [0] + alist
        while i > 0:
            self.downHeap(i)
            i = i - 1

    def buildHeapTup(self):
        i = len(self) // 2
        while i > 0:
            self.downHeapTup(i)
            i = i - 1

    def downHeapTup(self, i):
        while i * 2 <= len(self):
            mc = self.min_childTup(i)
            if self.items[i][1] < self.items[mc][1]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_childTup(self, i):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.items[i * 2][1] < self.items[i * 2 + 1][1]:
            return i * 2

        return i * 2 + 1

    def delete_minTup(self):
        return_value = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.downHeapTup(1)
        return return_value
#tests to ensure max heap

info = [ ( 1, 2), (3, 4), (5, 6) ]

heaptest = BinaryHeap()
heaptest.insert((98, 17))
heaptest.insert((9, 23))
heaptest.insert((99, 25))
heaptest.insert((1000, 3))
heaptest.insert((45, 30))
print(heaptest.items)
#heaptestShuffle = BinaryHeap()
heaptestShuffle = heaptest
print("shuffle",heaptestShuffle.items)
#heaptestShuffle.buildHeapTup()
for i in range(1,len(heaptestShuffle)):
    heaptestShuffle.downHeapTup(i)
print("sorted",heaptestShuffle.items)
print(heaptest.delete_minTup())
print(heaptest.delete_minTup())
print(heaptest.delete_minTup())
"""
heaptest = BinaryHeap()
heaptest.insert(98)
heaptest.insert(99)
heaptest.insert(1000)

print(len(heaptest))
print(heaptest.items)
print(heaptest.delete_min())
print(heaptest.delete_min())

lol = BinaryHeap()
test = [11,2,44,54,3,5,677,8,8,65,4,3,2]
lol.buildHeap(test)
print(heaptest.items)
"""
