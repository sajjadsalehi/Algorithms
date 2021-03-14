def search(text, pat):
    n = len(text)
    m = len(pat)
    skip = 0

    right = {}
    for c in text:
        right[c] = -1
    for j in range(0, m):
        right[pat[j]] = j

    i = 0
    while i < n-m:
        skip = 0
        for j in range(m-1, 0, -1):
            if pat[j] != text[i+j]:
                skip = max(1, j - right[text[i+j]])
                break
        if skip == 0:
            return i
        i += skip

    return n

