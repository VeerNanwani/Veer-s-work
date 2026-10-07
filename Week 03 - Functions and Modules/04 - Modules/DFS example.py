graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": [],
    "G": ["L", "M"],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": []
}

stack = ["A"]
visited = []

while stack:
    node = stack.pop()

    if node not in visited:
        visited.append(node)

        for neighbour in reversed(graph[node]):
            stack.append(neighbour)

print(visited)