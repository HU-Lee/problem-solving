from sys import stdin

r,c,k = map(int, stdin.readline().split())

maps = []
for i in range(r):
    maps.append(list(stdin.readline().strip()))

visited = [[False]*c for _ in range(r)]
visited[r-1][0] = True

answer = 0

def dfs(x,y,distance) -> int:
    global answer
    if x==c-1 and y==0 and distance == k:
        answer += 1
        return
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        if (
            0 > x+dx or x+dx >= c
            or 0 > y+dy or y+dy >= r
        ):
            continue
        if (
            maps[y+dy][x+dx] != "T" 
            and not visited[y+dy][x+dx]
        ):
            visited[y+dy][x+dx] = True
            dfs(x+dx,y+dy,distance+1)
            visited[y+dy][x+dx] = False
    return

dfs(0,r-1,1)
print(answer)