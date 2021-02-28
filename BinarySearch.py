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
