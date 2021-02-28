import random


class QuickSort:

    def partition(self, a, low, high):
        i = low
        j = high+1
        while True:
            i += 1
            while a[i] < a[low]:
                if i == high:
                    break
                i += 1
            j -= 1
            while a[low] < a[j]:
                if j == low:
                    break
                j -= 1

            if i >= j:
                break
            self.swap(a, i, j)

        self.swap(a, low, j)
        return j

    def swap(self, a, i, j):
        temp = a[j]
        a[j] = a[i]
        a[i] = temp

    def sort(self, a):
        random.shuffle(a)
        self.qsort(a, 0, len(a)-1)
        return a

    def qsort(self, a, low, high):
        if high <= low:
            return
        j = self.partition(a, low, high)
        self.qsort(a, low, j-1)
        self.qsort(a, j+1, high)

