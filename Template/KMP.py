#next array
def na(s):
    n = len(s)
    nxt = [0] * n
    for i in range(1, n):
        j = nxt[i - 1]
        while j > 0 and s[i] != s[j]:
            j = nxt[j - 1]
        if s[i] == s[j]:
            nxt[i] = j + 1
    return nxt

def KMP(s, t):
    nxt = na(t)
    m = len(t)
    i = 0
    j = 0
    # res = 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        elif j:
            j = nxt[j - 1]
        else:
            i += 1
        if j == m:
            # res += 1
            # j = nxt[j - 1]    calculate the counts of matches
            return i - j