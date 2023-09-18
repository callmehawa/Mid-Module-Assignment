import sys

# Define infinity
INF = "NO_PATH"

# Sample graph
graph = [
    [0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]
]

def floyd_recursive(graph, i, j, k):
    """
    Recursive Floyd-Warshall algorithm to compute shortest distances.
    DEFINE THE PARAMETERS HERE
    """
    if k < 0:
        return graph

    if i == j:
        return graph

    if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

    if i < len(graph) - 1:
        if j < len(graph) - 1:
            return floyd_recursive(graph, i, j + 1, k)
        else:
            return floyd_recursive(graph, i + 1, 0, k)
    else:
        if j < len(graph) - 1:
            return floyd_recursive(graph, 0, j + 1, k)
        else:
            return floyd_recursive(graph, 0, 0, k - 1)

# Call the recursive function to compute shortest distances
result = floyd_recursive(graph, 0, 0, 0)

# Print the result
for row in result:
    print(row)

