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
            # Only read in the first 3 elements for each line to avoid comments
            # u, v, gas_prices, distance = map(int, line.split()[:4])

            # Parse line, storing cities, distances, & gas price for that stretch
            parts = line.split()[:4] # Split first four elements
            u, v = map(int, parts[:2]) # Conv to ints
            gas_price = float(parts[2]) # Conv to float
            distance = int(parts[3]) # Conv to int


            # Updates adjacency list to add undirected edges between cities u & v
            graph[u].append((v, distance, gas_price))
            graph[v].append((u, distance, gas_price))

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
        for v, dist_to_v, _ in graph[u]:
            # Checks both:
            # If city 'v' has not been visited 
            # AND if distance from start to 'v' via 'u' is shorter than known shortest distance thus far
            if not visited[v] and dist_u + dist_to_v < distance[v]:
                # If so, update shortest distance to 'v' & records 'u' as previous city on shortest path to 'v'
                distance[v] = dist_u + dist_to_v
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


def calc_fuel_cost(path, graph, tank_size, fuel_efficiency):
    total_cost = 0
    fuel_left = tank_size  # Assume we start with a full tank

    # Iterate over current path
    for i in range(len(path) - 1):
        u = path[i]  # Set u as current city
        v = path[i + 1]  # Set v as next city
    
        # Finds edge connecting current city to next
        edge = next((edge for edge in graph[u] if edge[0] == v), None)

        # Set distance & gas_price for calculation based on graph information
        # Sets distance & price for this route
        distance, gas_price = edge[1], edge[2]
        fuel_needed = distance / fuel_efficiency

        # If you run out of gas, refuel
        if fuel_needed > fuel_left:
            # Calc cost to refuel tank completely and add to total_cost
            total_cost += (tank_size - fuel_left) * gas_price
            fuel_left = tank_size

        # Minus fuel for this stretch
        fuel_left -= fuel_needed

    return total_cost



def main():

    # Default values for fuel calcs
    tank_size = 60 # Tank size in liters
    fuel_efficiency = 4 # liters/km ?

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

        # Calc fuel cost
        total_cost = calc_fuel_cost(shortest_path, graph, tank_size, fuel_efficiency)
        # Prints value for shortest distance, then the city numbers in that path
        print(f"Shortest distance: {shortest_distance}km")
        print("Shortest path:", " -> ".join(map(str, shortest_path)))
        print(f"Total fuel cost:  €{total_cost:0.2f}")
    else:
        print("Invalid city numbers. Please enter valid city numbers.")


if __name__ == "__main__":
    main()
