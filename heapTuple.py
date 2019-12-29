# implementation of Priority Queue using heap with tuple elements
# Depending on the person passed in, the queue will work based off the correct set of data
class PriorityQueue(object):
    def __init__(self):
        self.items = [0]
    # Overwrite the len function for this object
    def __len__(self):
        return len(self.items) - 1

    # Standard upheap function
    def upHeap(self, person):
        i = len(self)
        while i // 2 > 0:
            if self.items[i][person] > self.items[i // 2][person]:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2

    # Function to insert tuple
    def insert(self, item, person):
        self.items.append(item)
        self.upHeap(person)

    # Standard downheap function
    def downHeap(self, i, person):
        while i * 2 <= len(self):
            mc = self.minChild(i, person)
            if self.items[i][person] < self.items[mc][person]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    # Function to find the minimum child
    def minChild(self, i,person ):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.items[i * 2][person] > self.items[i * 2 + 1][person]:
            return i * 2
        return i * 2 + 1

    # Return front of the queue then resort
    def removeMax(self,person):
        if len(self) == 0:
            return (0,0)
        max = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.downHeap(1, person)
        return max

    # Check next item without popping from queue
    def peek(self):
        return self.items[1]

    # Completely resort heap
    def heapify(self, person):
        i = len(self.items)
        while i > 0:
            self.downHeap(i,person)
            i = i - 1
