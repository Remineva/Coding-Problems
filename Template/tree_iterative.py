def solve():
    n = int(input())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    #calculate the number of children for each node
    cnt = [1] * n
    visited = [True] * n
    visited[0] = False
    parent = [-1] * n
    q = []
    q.append((0, 1))
    while q:
        i, task= q.pop()
        if task == 0:
            for j in g[i]:
                if j != parent[i]:
                    cnt[i] += cnt[j]
        else:
            q.append((i, 0))
            visited[i] = False
            for j in g[i]:
                if visited[j]:    
                    q.append((j, 1))
                    parent[j] = i
    
    #calculate the answer for root 0
    output = [0] * n
    stack = [0]
    while stack:
        i = stack.pop()
        for j in g[i]:
            if j != parent[i]:
                output[0] += #condition
                stack.append(j)
    
    #reroot
    stack = [0]
    while stack:
        i = stack.pop()
        for j in g[i]:
            if j != parent[i]:
                output[j] = #transition condition
                stack.append(j)

    print(*output)