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
                self.items[i // 2], self.items[i] = \
                self.items[i], self.items[i // 2]
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

    def build_heap(self, alist):
        i = len(alist) // 2
        self.items = [0] + alist
        while i > 0:
            self.downHeap(i)
            i = i - 1

#tests to ensure max heap
heaptest = BinaryHeap()
heaptest.insert(4)
heaptest.insert(9)
heaptest.insert(5)
heaptest.insert(4)
heaptest.insert(2)
print(len(heaptest))
print(heaptest.items)
print(heaptest.delete_min())
print(heaptest.delete_min())

lol = BinaryHeap()
test = [11,2,44,54,3,5,677,8,8,65,4,3,2]
lol.build_heap(test)
print(heaptest.items)
