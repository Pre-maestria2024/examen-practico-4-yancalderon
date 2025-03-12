from queue import PriorityQueue
from queue import Queue
from collections import defaultdict, deque

def build_tree(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def orient_tree(adj, n, root=0):
    parent = [-1] * n
    depth = [0] * n
    stack = [(root, -1, 0)]
    children = defaultdict(list)
    
    while stack:
        node, par, d = stack.pop()
        parent[node] = par
        depth[node] = d
        for neighbor in adj[node]:
            if neighbor != par:
                children[node].append(neighbor)
                stack.append((neighbor, node, d + 1))
    
    return parent, depth, children

def longest_path_to_leaf(children, depth, n):
    longest = [0] * n
    
    def dfs(node):
        if not children[node]:
            longest[node] = depth[node] + 1
            return longest[node]
        
        max_child_path = 0
        for child in children[node]:
            max_child_path = max(max_child_path, dfs(child))
        longest[node] = max_child_path
        return longest[node]
    
    dfs(0)
    return longest

def max_groups(n, k, edges):
    if k == 0:
        return 0
    if k == 1:
        return n
    
    adj = build_tree(n, edges)
    
    parent, depth, children = orient_tree(adj, n)
    
    longest = longest_path_to_leaf(children, depth, n)
    
    used = [False] * n
    total_groups = 0
    
    def assign_groups(node, path_len):
        nonlocal total_groups
        num_groups = path_len // k
        curr = node
        for _ in range(num_groups):
            group_cabins = []
            temp = curr
            for _ in range(k):
                if temp == -1 or used[temp]:
                    return
                group_cabins.append(temp)
                temp = parent[temp]
            for cabin in group_cabins:
                used[cabin] = True
            total_groups += 1
            for _ in range(k):
                if curr != -1:
                    curr = parent[curr]
    
    nodes_by_depth = sorted(range(n), key=lambda x: depth[x], reverse=True)
    for node in nodes_by_depth:
        if not used[node]:
            path_len = depth[node] + 1
            assign_groups(node, path_len)
    
    return total_groups

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    result = max_groups(n, k, edges)
    print(result)

if __name__ == '__main__':
    main() 