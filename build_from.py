class NaryHeap:
    def __init__(self, branching_factor=2):
        self.heapList = [0]
        self.currentSize = 0
        self.branching_factor = branching_factor

    def percUp(self, i):
        parent = i // self.branching_factor
        while parent > 0:
            if self.heapList[i] < self.heapList[parent]:
                self.heapList[i], self.heapList[parent] = self.heapList[parent], self.heapList[i]
            i = parent
            parent = i // self.branching_factor

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while i * self.branching_factor <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        start = i * self.branching_factor
        end = min((i + 1) * self.branching_factor, self.currentSize + 1)
        return min(range(start, end), key=lambda x: self.heapList[x])

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // self.branching_factor
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    def __str__(self):
        def visualize_tree(i):
            if i > self.currentSize:
                return ''
            children = [visualize_tree(j) for j in range(i*self.branching_factor, (i+1)*self.branching_factor)]
            children = [c for c in children if c]
            return '[{} {}]'.format(self.heapList[i], ' '.join(children))
        
        return visualize_tree(1)


bh = NaryHeap(3)
bh.buildHeap([9, 5, 6, 2, 3, 7, 8, 4])

print(bh)
