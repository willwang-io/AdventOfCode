from collections import defaultdict

def dfs(u, adj, vis, cur=0):
    if u not in vis and len(vis) + 1 == len(adj):
        return cur
    vis.add(u)
    ans = 0
    for v, w in adj[u]:
        if v not in vis:
            ans = max(ans, dfs(v, adj, vis, cur + w))
    vis.remove(u)
    return ans

def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()

    edges = []
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        line = line.strip()
        loc, val = line.split(" = ")
        p, q = loc.split(" to ")
        adj[p].append((q, int(val)))
        adj[q].append((p, int(val)))
    ans = 0
    for u in adj:
        ans = max(ans, dfs(u, adj, set()))
    print(ans)

if __name__ == "__main__":
    main()

