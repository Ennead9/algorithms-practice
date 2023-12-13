import heapq

# Read input data from 'input.txt' file (in same directory)
def read_input(filename):
    with open(filename, 'r') as file:
        # Read in the # of cities (aka vertices)
        n = int(file.readline())
        # Make empty graph with this number of vertices
        graph = [[] for _ in range(n)]

        # Gets the connections (aka edges) between cities and their values (representing distances)
        for line in file:
            # Parse line, storing cities and their distances
            u, v, distance = map(int, line.strip().split())
            # Adds edges between cities u & v (in both directions)
            graph[u].append((v, distance))
            graph[v].append((u, distance))

    return n, graph

# Dijkstra's algorithm implementation
def dijkstra(n, graph, start, end):
    visited = [False] * n   # List that tracks cities we've already visited
    distance = [float('inf')] * n  # List to track shortest distance to each city
    previous = [-1] * n    # List to track previous city in shortest path

    # Set distance to the starting city at 0 of course
    distance[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        dist_u, u = heapq.heappop(min_heap) # gets the city with shortest distance from min heap

        # Stops when we reach the destination city
        if u == end:
            break

        # Skip cities which are already visited
        if visited[u]:
            continue

        visited[u] = True   # Label current city as visited

        # Find neighboring cities & update distances if we find a shorter path
        for v, w in graph[u]:
            if not visited[v] and dist_u + w < distance[v]:
                distance[v] = dist_u + w
                previous[v] = u
                heapq.heappush(min_heap, (distance[v], v))

    path = []
    u = end
    while u != -1:
        path.append(u)
        u = previous[u]

    return distance[end], path[::-1]

def main():
    input_filename = 'input.txt'
    n, graph = read_input(input_filename)

    start_city = int(input("Enter the start city number: "))
    end_city = int(input("Enter the destination city number: "))

    if 0 <= start_city < n and 0 <= end_city < n:
        shortest_distance, shortest_path = dijkstra(n, graph, start_city, end_city)
        print(f"Shortest distance: {shortest_distance}")
        print("Shortest path:", " -> ".join(map(str, shortest_path)))
    else:
        print("Invalid city numbers. Please enter valid city numbers.")


if __name__ == "__main__":
    main()
