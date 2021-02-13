class BinarySearch:

    def search(self, a, key):
        lo = 0
        hi = len(a)-1

        while lo <= hi:
            mid = int(lo + (hi-lo)/2)
            if key < a[mid]:
                hi = mid-1
            elif key > a[mid]:
                lo = mid+1
            else:
                return mid

        return -1


if __name__ == '__main__':
    lst = [12, 43, 52, 71, 86, 98, 108]
    bSearch = BinarySearch()
    position = bSearch.search(lst, 98)
    print(position)
