class MergeSort:

    def sort(self, a):
        aux = [None]*len(a)
        self.msort(a, aux, 0, len(a))
        return a

    def msort(self, a, aux, low, high):
        if high <= low:
            return
        mid = int(low + (high - low)/2)
        self.msort(a, aux, mid+1, high)
        self.msort(a, aux, low, mid)
        self.merge(a, aux, low, mid, high)

    def merge(self, a, aux, low, mid, high):
        for k in range(low, high):
            aux[k] = a[k]

        i = low
        j = mid+1
        for k in range(low, high):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j >= high:
                a[k] = aux[i]
                i += 1
            elif (aux[j] is not None
                  and aux[i] is not None) and aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
            else:
                a[k] = a[i]
                i += 1


