class InsertionSort:
    def sort(self, a):
        n = len(a)
        for i in range(n):
            for j in range(i, n):
                if a[j] < a[j-1]:
                    self.swap(a, j, j-1)
                else:
                    break
        return a

    def swap(self, a, i, j):
        temp = a[j]
        a[j] = a[i]
        a[i] = temp


if __name__ == '__main__':
    insertion_sort = InsertionSort()
    a = [1, 90, 73, 12, 2, 24]
    sorted_array = insertion_sort.sort(a)
    print(sorted_array)
