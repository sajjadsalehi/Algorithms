def sort(a, R):
    n = len(a)
    count = [0]*(R+1)
    for i in range(n):
        count[a[i]+1] = count[a[i]+1]+1

    for r in range(R):
        count[r+1] += count[r]

    aux = [-1]*n
    for i in range(n):
        aux[count[a[i]]] = a[i]
        count[a[i]] += 1

    for i in range(n):
        a[i] = aux[i]

