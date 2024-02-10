class SegmentTree:
    
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
    
    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n>>1] = self.tree[n] + self.tree[n^1]
            n >>= 1
    
    def sumRange(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


class LazySegTree:
    
    def __init__(self, nums):
        n = len(nums)
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

        def build(o, l, r):
            if l == r:
                self.tree[o] = nums[l - 1]
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]
    
        build(1, 1, n)
        
    def update(self, o, l, r, L, R, add):
        if L <= l and r <= R:
            self.tree[o] += (r - l + 1) * add
            self.lazy[o] += add
            return
        m = (l + r) // 2
        if self.lazy[o] != 0 and l != r:
            self.tree[o * 2] += self.lazy[o] * (m - l + 1)
            self.tree[o * 2 + 1] += self.lazy[o] * (r - m)
            self.lazy[o * 2] += self.lazy[o]
            self.lazy[o * 2 + 1] += self.lazy[o]
            self.lazy[o] = 0
        if m >= L:
            self.update(o * 2, l, m, L, R, add)
        if m < R:
            self.update(o * 2 + 1, m + 1, r, L, R, add)
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]

    def query(self, o, l, r, L, R):
        if L <= l and r <= R:
            return self.tree[o]
        m = (l + r) // 2
        if self.lazy[o] != 0:
            self.tree[o * 2] += self.lazy[o] * (m - l + 1)
            self.tree[o * 2 + 1] += self.lazy[o] * (r - m)
            self.lazy[o * 2] += self.lazy[o]
            self.lazy[o * 2 + 1] += self.lazy[o]
            self.lazy[o] = 0
        s = 0
        if m >= L:
            s = self.query(o * 2, l, m, L, R)
        if m < R:
            s += self.query(o * 2 + 1, m + 1, r, L, R)
        return s

#flip, max
M = 10 ** 9 + 7
class LazySegTree:
    
    def __init__(self, nums):
        n = len(nums)
        self.tree = [0] * (4 * n)
        self.lazy = [False] * (4 * n)
        self.idx = [-1] * (4 * n)
        self.flip = [0] * (4 * n)
        self.fi = [-1] * (4 * n)

        def build(o, l, r):
            if l == r:
                self.tree[o] = nums[l - 1]
                self.idx[o] = l
                self.flip[o] = nums[l - 1]
                self.fi[o] = l
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            if self.tree[o * 2] >= self.tree[o * 2 + 1]:
                self.tree[o] = self.tree[o * 2]
                self.idx[o] = self.idx[o * 2]
            else:
                self.tree[o] = self.tree[o * 2 + 1]
                self.idx[o] = self.idx[o * 2 + 1]
            if self.flip[o * 2] <= self.flip[o * 2 + 1]:
                self.flip[o] = self.flip[o * 2]
                self.fi[o] = self.fi[o * 2]
            else:
                self.flip[o] = self.flip[o * 2 + 1]
                self.fi[o] = self.fi[o * 2 + 1]
    
        build(1, 1, n)
        
    def push(self, o):
        self.tree[o], self.flip[o] = M - self.flip[o], M - self.tree[o]
        self.idx[o], self.fi[o] = self.fi[o], self.idx[o]
        self.lazy[o] = not self.lazy[o]

    def update(self, o, l, r, L, R):
        if L <= l and r <= R:
            self.push(o)
            return
        m = (l + r) // 2
        if self.lazy[o]:
            self.push(o * 2)
            self.push(o * 2 + 1)
            self.lazy[o] = False
        if m >= L:
            self.update(o * 2, l, m, L, R)
        if m < R:
            self.update(o * 2 + 1, m + 1, r, L, R)
        if self.tree[o * 2] >= self.tree[o * 2 + 1]:
            self.tree[o] = self.tree[o * 2]
            self.idx[o] = self.idx[o * 2]
        else:
            self.tree[o] = self.tree[o * 2 + 1]
            self.idx[o] = self.idx[o * 2 + 1]
        if self.flip[o * 2] <= self.flip[o * 2 + 1]:
            self.flip[o] = self.flip[o * 2]
            self.fi[o] = self.fi[o * 2]
        else:
            self.flip[o] = self.flip[o * 2 + 1]
            self.fi[o] = self.fi[o * 2 + 1]

    def query(self):
        return self.idx[1]

#Dynamic Node
class TreeNode:
    def __init__(self, l = None, r = None, v = -1):
        self.l = l
        self.r = r
        self.val = v
     
    
class SegmentTree:
    def __init__(self):
        self.root = TreeNode()
    
    def update_from(self, node):
        node.val = max(node.l.val if node.l else -1, node.r.val if node.r else -1)
        return node
    
    def update(self, node, l, r, i, val):
        if i < l or i > r:
            return None
        if not node:
            node = TreeNode()
        if l == r:
            node.val = val
            return node
        mid = (l + r) // 2
        if i <= mid:
            node.l = self.update(node.l, l, mid, i, val)
        else:
            node.r = self.update(node.r, mid + 1, r, i, val)
        return self.update_from(node)
    
    def query(self, node, l, r, x, y):
        if not node or y < l or x > r:
            return -1
        if x <= l and y >= r:
            return node.val
        mid = (l + r) // 2
        res = -1
        if x <= mid:
            res = self.query(node.l, l, mid, x, y)
        if y > mid:
            res = max(res, self.query(node.r, mid + 1, r, x, y))
        return res
