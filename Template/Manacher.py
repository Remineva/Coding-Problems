#odd
def manacher(s):
    n = len(s)
    d1 = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else min(d1[l + r - i], r - i + 1)
        while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
            k += 1
        d1[i] = k
        k -= 1
        if i + k > r:
            l = i - k
            r = i + k
    return d1

#even
def manacher(s):
    n = len(s)
    d2 = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        k -= 1
        if i + k > r:
            l = i - k - 1
            r = i + k
    return d2

print(manacher('ababbabb'))

def longestPalindrome(s):
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    c = r = 0
    
    for i in range(1, n - 1):
        m = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[m])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > r:
            c = i
            r = i + p[i]
            
    maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
    return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [1] * n
        m = r = 1
        
        for i in range(2, n - 1):
            if i < r:
                p[i] = min(p[2 * m - i], r - i + 1)
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i + p[i] - 1 > r:
                r = i + p [i] - 1
                m = i
                
        maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
        t = t[centerIndex - maxLen + 1: centerIndex + maxLen]
        return t.replace('#', '')