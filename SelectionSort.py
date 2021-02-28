class SelectionSort:

    def sort(self, a):
        n = len(a)
        for i in range(n):
            min = i
            for j in range(i, n):
                if a[j] < a[min]:
                    min = j
            self.swap(a, i, min)
        return a

    def swap(self, a, i, min):
        temp = a[min]
        a[min] = a[i]
        a[i] = temp


