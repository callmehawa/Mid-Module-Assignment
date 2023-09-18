
# Defining infinity as NO_PATH"
INF = "NO_PATH"

def floyd_recursive(graph, i, j, k):
    """
    Floyd-Warshall algorithm to calculate shortest path between two nodes and solved recursively using a recursive function.
    
    Parameters:
    graph - Input weighted directed 4X4 matrix graph
    i (int) - the source node for the shortest path calculation.
    j (int) - destination node for the shortest path calculation.
    k (int) - intermediate node for the shortest path calculation.
    
    Returns:
    matrix containing the shortest path between all pairs of nodes.

    """
    # base case - source node = destinate node path distance is zero therefore return to matrix witout update

    if i == j:
        return graph
    
    #calculate shortests distance through intermediate node. If this distance is smaller than the current distance stored 
    # in the graph, it will the graph with the shorter distance

    if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

    if i < len(graph) - 1: # check to identify end of the row
        if j < len(graph) - 1: # check to identify end of the column
            return floyd_recursive(graph, i, j + 1, k) # if it is not end of the column, it increments the column "j" by 1 to find the next shortest path
        else:
            return floyd_recursive(graph, i + 1, 0, k) # if it is end of the column, it resets the column to zero and increments "i" by 1 to move to next row
    else:
        if j < len(graph) - 1: # check to see if there are more column to process
            return floyd_recursive(graph, 0, j + 1, k) #if true "j" column is incremented by 1 tp proces remaing column
        else:
            return floyd_recursive(graph, 0, 0, k - 1) # once all rows and columns are processed, intermediate is decremented by 1 to move to the next intermediate node.


# Input graph
graph = [
    [0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]
]

# Call the recursive function to compute shortest distances
result = floyd_recursive(graph, 0, 0, 0)


# Print the result to show the shortest path for all vertices.
for row in result:
    print(row)
