import heapq

# Read input data from file, then constructs the graph
# Returns a tuple of the number of cities (n) and the constructed graph (graph)
def read_input(filename):
    with open(filename, 'r') as file:

        n = int(file.readline().strip())  # Read in number of cities (aka vertices)
        
        # Initialize adjacency list with one empty list for each city (vertex)
        graph = [[] for _ in range(n)]

        # Gets the connections (aka edges) between cities and their values (representing distances)
        for line in file:
            # Split the line at the first occurrence of '#' and process the first part
            line = line.split('#')[0].strip()
            
            # End upon first empty line9
            if not line:
                break

            # Parse line, storing cities and their distances
            parts = line.split()
            if len(parts) != 3:
                continue  # Skip lines that do not have exactly 3 elements

            # Parse line, storing cities and their distances
            # Only read in the first 3 elements for each line to avoid comments
            u, v, distance = map(int, line.split()[:3])

            # Updates adjacency list to add undirected edges between cities u & v
            graph[u].append((v, distance))
            graph[v].append((u, distance))

    return n, graph

# Dijkstra's algorithm implementation
def dijkstra(n, graph, start, end):
    '''
    n is number of total cities (nodes/vertices)
    graph is a graph represented as adjacency lists
    start: Starting city/vertex
    end: Destination city/vertex

    Returns the shortest distance and the shortest path from start to end city
    '''
    # List of bools to track whether cities have already been visited
    visited = [False] * n
    # List of floats to track shortest known distance to each city from start city
    distance = [float('inf')] * n
    # List to track previous city for each city on the shortest path from start
    # Important: Initializes all to -1 to denote "No known path yet"
    previous = [-1] * n

    # Set distance to the starting city at 0 of course
    distance[start] = 0
    min_heap = [(0, start)]  # min_heap to prioritize vertices with shortest distance

    while min_heap:
        dist_u, u = heapq.heappop(min_heap) # Gets city with shortest distance from min heap

        # Stops when we reach the destination city
        if u == end:
            break

        # Skip cities which are already visited
        if visited[u]:
            continue

        visited[u] = True   # Label current city as 'visited'

        # Update distances for neighboring cities
        # Iterate over neighboring cities of current city 'u'
        for v, w in graph[u]:
            # Checks both:
            # If city 'v' has not been visited 
            # AND if distance from start to 'v' via 'u' is shorter than known shortest distance thus far
            if not visited[v] and dist_u + w < distance[v]:
                # If so, update shortest distance to 'v' & records 'u' as previous city on shortest path to 'v'
                distance[v] = dist_u + w
                previous[v] = u
                # Finally, pushes 'v' onto priority queue with its updated distance
                heapq.heappush(min_heap, (distance[v], v))

    path = []  # To store the shortest path
    u = end    # Start backtracking from destination city

    # Backtracks from destination city to start city to reconstruct the shortest path
    while u != -1:
        path.append(u)
        u = previous[u]

    return distance[end], path[::-1]  # Return shortest distance & path, in reverse order

def main():

    # Reads 'input.txt' file, storing value for n and constructing graph
    input_filename = 'input.txt'
    n, graph = read_input(input_filename)

    # Prompts user for start and destination cities
    start_city = int(input("Enter city of origin number: "))
    end_city = int(input("Enter the destination city number: "))

    # Validate that numbers entered are within range (0, n-1)
    if 0 <= start_city < n and 0 <= end_city < n:
        
        # Calls Dijkstra to find shortest path
        shortest_distance, shortest_path = dijkstra(n, graph, start_city, end_city)

        # Prints value for shortest distance, then the city numbers in that path
        print(f"Shortest distance: {shortest_distance}km")
        print("Shortest path:", " -> ".join(map(str, shortest_path)))
    else:
        print("Invalid city numbers. Please enter valid city numbers.")


if __name__ == "__main__":
    main()
