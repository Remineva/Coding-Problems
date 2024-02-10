edges = []
n = 1
g = [[] for _ in range(n)]
for a, b, w in edges:
    g[a].append((b, w))
    g[b].append((a, w))
    

idx, lo_link = [None for _ in range(n)], [None for _ in range(n)]
stack, on_stack, unvisited = [], set(), set(range(n))
for i in range(n):
    if lo_link[i] != None:
        continue
    dfs = [(i, -1)]
    curr_idx = i
    while dfs:
        node, predecessor = dfs[-1]
        unvisited.discard(node)
        if node not in on_stack:
            stack.append(node)
            on_stack.add(node)
        if idx[node] is None:
            idx[node] = curr_idx
            lo_link[node] = curr_idx
            curr_idx = curr_idx + 1
        for ls in g[node]:
            neighbor, _ = ls
            if neighbor != predecessor:
                if neighbor in unvisited:
                    dfs.append((neighbor, node))
                    break
                if neighbor in on_stack:
                    lo_link[node] = min(lo_link[node], lo_link[neighbor])
        if dfs[-1][0] != node:
            continue
        if lo_link[node] == idx[node]:
            while node in on_stack:
                lo_link[stack[-1]] = lo_link[node]
                on_stack.remove(stack.pop())
        dfs.pop()