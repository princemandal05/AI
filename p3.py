# A Star Algorithm Using Heuristic Method

def heuristic(n):
    h_dist = {
        'A': 11,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 2,
        'J': 0
    }
    return h_dist[n]


graph_node = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2), ('A', 6)],
    'C': [('E', 5), ('B', 3), ('D', 1)],
    'D': [('C', 1), ('B', 2), ('E', 8)],
    'E': [('J', 0), ('I', 5), ('D', 8), ('C', 5)],
    'F': [('G', 5), ('H', 3), ('A', 3)],
    'G': [('I', 1), ('F', 1)],
    'H': [('F', 7), ('I', 2)],
    'I': [('C', 3), ('E', 5), ('G', 1), ('H', 2)],
    'J': [('E', 5), ('I', 3)]
}


def a_star(start, goal):
    open_list = [(heuristic(start), 0, start)]
    closed_list = []
    parent = {}
    g_cost = {start: 0}

    while open_list:
        open_list.sort()
        f, g, current = open_list.pop(0)

        if current in closed_list:
            continue

        if current == goal:
            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path, g

        closed_list.append(current)

        for neighbour, cost in graph_node[current]:
            new_g = g + cost

            if neighbour in closed_list:
                continue

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                parent[neighbour] = current
                f_cost = new_g + heuristic(neighbour)
                open_list.append((f_cost, new_g, neighbour))

    return None, None


start = 'A'
goal = 'J'

path, cost = a_star(start, goal)

if path:
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
