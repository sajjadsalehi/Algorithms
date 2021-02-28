class HeapSort:

    def exchange(self, a, item1, item2):
        temp = a[item1]
        a[item1] = a[item2]
        a[item2] = temp

    def sink(self, a, k, n):
        while 2*k < n:
            j = 2*k
            if j+1 < n and a[j] < a[j+1]:
                j += 1
            if a[k] >= a[j]:
                break
            self.exchange(a, k, j)
            k = j

    def sort(self, a):
        a.insert(0, None)
        n = len(a)
        for k in range(int(n/2), 0, -1):
            self.sink(a, k, n)

        while n > 1:
            self.exchange(a, 1, n-1)
            n -= 1
            self.sink(a, 1, n)

        a.pop(0)
