with open('input.txt','r') as file:
    heightmap = {i +j*1j: int(value) for i, line in enumerate(file) for j, value in enumerate(line.strip())}

possible_moves = [1,-1,1j,-1j]
graph = dict()
for pos in heightmap:
    moves = [pos + i for i in possible_moves if pos + i in heightmap and heightmap[pos+i]==heightmap[pos]+1]
    graph[pos] = moves

def dfs(graph, start, end, visited=None):
    if visited is None:
        visited = set()    
    if start == end:
        return 1
    visited.add(start)
    path_count = 0
    for neighbour in graph[start]:
        if neighbour not in visited:
            path_count += dfs(graph,neighbour, end, visited)
    visited.remove(start)

    return path_count

starts = []
ends = []

for node in heightmap:
    if heightmap[node] == 0:
        starts.append(node)
    elif heightmap[node] == 9:
        ends.append(node)

total_paths = 0
is_path = 0

for start in starts:
    for end in ends:
        paths =  dfs(graph,start,end)
        total_paths += paths
        if paths:
            is_path += 1


print(f"Part 1 {is_path}")
print(f"Part 2 {total_paths}")