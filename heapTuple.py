class PriorityQueue(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    #parent node = node position / 2
    def upHeap(self, person):
        i = len(self)
        while i // 2 > 0:
            if self.items[i][person] > self.items[i // 2][person]:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, item, person):
        self.items.append(item)
        self.upHeap(person)


    def downHeap(self, i, person):
        while i * 2 <= len(self):
            mc = self.min_child(i, person)
            if self.items[i][person] < self.items[mc][person]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    #can this be simplified to the last val in array
    def min_child(self, i,person ):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.items[i * 2][person] > self.items[i * 2 + 1][person]:
            return i * 2
        return i * 2 + 1

    def removeMax(self,person):
        if len(self) == 0:
            return (0,0)
        max = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.downHeap(1, person)
        return max

    def peek(self):
        return self.items[1]

    def heapify(self, person):
        i = len(self.items)
        while i > 0:
            self.downHeap(i,person)
            i = i - 1
