class InsertionSort:
    def sort(self, a):
        n = len(a)
        for i in range(n):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    self.swap(a, j, j-1)
                else:
                    break
        return a

    def swap(self, a, i, j):
        temp = a[j]
        a[j] = a[i]
        a[i] = temp


