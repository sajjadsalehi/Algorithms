class ShellSort:
    def sort(self, a):
        n = len(a)

        h = 1
        while h < n/3:
            h = 3*h+1

        while h >= 1:
            for i in range(h, n):
                for j in range(i, h, -h):
                    if j >= h and a[j] < a[j - h]:
                        self.swap(a, j, j - h)
                    else:
                        break
            h = int(h/3)
        return a

    def swap(self, a, i, j):
        temp = a[j]
        a[j] = a[i]
        a[i] = temp


