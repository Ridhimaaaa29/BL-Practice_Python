from collections import deque


def bidirectional_bfs(graph, start, destination):
    """
    Bidirectional BFS searches from both the start and
    destination at the same time and stops when the two
    searches meet at a comman point.

    This is suitable for unweighted graphs where every
    road represents one movement.

    Returns:
        tuple:
            path          - shortest path as a list
            steps         - number of roads in the path
            nodes_visited - total nodes visited by both searches
    """

    # If start and destination are the same, no movement is required.
    if start == destination:
        return [start], 0, 1

    # If either node does not exist in the graph, no route can be found.
    if start not in graph or destination not in graph:
        return [], 0, 0

    # Queue for searching from the starting location.
    forward_queue = deque([start])

    # Queue for searching backwards from the destination.
    backward_queue = deque([destination])

    # Nodes already visited from each direction.
    forward_visited = {start}
    backward_visited = {destination}

    # Parent dictionaries are used to reconstruct the actual path after the two searches meet.
    forward_parent = {start: None}
    backward_parent = {destination: None}

    while forward_queue and backward_queue:

        # Expand the forward search.
        current = forward_queue.popleft()

        for neighbor in graph.get(current, []):

            if neighbor not in forward_visited:

                forward_visited.add(neighbor)
                forward_parent[neighbor] = current
                forward_queue.append(neighbor)

            # If the other search has already visited this node, the two searches have met.
            if neighbor in backward_visited:

                meeting_point = neighbor

                path = reconstruct_path(
                    forward_parent,
                    backward_parent,
                    meeting_point
                )

                steps = len(path) - 1
                nodes_visited = len(
                    forward_visited | backward_visited
                )

                return path, steps, nodes_visited

        # Expand the backward search.
        current = backward_queue.popleft()

        for neighbor in graph.get(current, []):

            if neighbor not in backward_visited:

                backward_visited.add(neighbor)
                backward_parent[neighbor] = current
                backward_queue.append(neighbor)

            # Check whether the forward search has already reached this node.
            if neighbor in forward_visited:

                meeting_point = neighbor

                path = reconstruct_path(forward_parent, backward_parent, meeting_point)

                steps = len(path) - 1
                nodes_visited = len(
                    forward_visited | backward_visited
                )

                return path, steps, nodes_visited

    # No route exists between the two locations.
    nodes_visited = len(
        forward_visited | backward_visited
    )

    return [], 0, nodes_visited


def reconstruct_path(
    forward_parent,
    backward_parent,
    meeting_point
):
    """
    Reconstruct the complete path after Bidirectional BFS
    finds a meeting point.

    The path is created in two parts:
        start -> meeting point
    and
        meeting point -> destination
    The duplicate meeting point is removed.
    """

    # Build start -> meeting point

    left_path = []

    current = meeting_point

    while current is not None:
        left_path.append(current)
        current = forward_parent[current]

    # Currently the path is reversed.
    left_path.reverse()

    # Build meeting point -> destination

    right_path = []

    current = meeting_point

    while current is not None:
        right_path.append(current)
        current = backward_parent[current]

    # If the meeting point appears in both lists. Remove it from the second list.
    final_path = left_path + right_path[1:]

    return final_path


def dfs(graph, start):
    """
    Performing Iterative Depth-First Search (DFS).

    DFS explores one branch as deeply as possible before
    backtracking.

    I used stack to avoid recursion and to keep track of the nodes to visit next.

    Returns:
        tuple:
            order        - order in which nodes were visited
            nodes_visited - number of nodes visited
    """

    # Stack used to implement DFS iteratively.
    stack = [start]

    # Set used to keep track of visited nodes.
    visited = set()

    # List used to store the traversal order.
    order = []

    while stack:

        # Remove the last element from the stack.
        current = stack.pop()

        # Skip the node if it has already been visited.
        if current in visited:
            continue

        # Mark the current node as visited.
        visited.add(current)

        # Store the node in traversal order.
        order.append(current)

        # Add unvisited neighbors to the stack.
        # reversed() is used so that the traversal order follows the adjacency-list order when using a stack.
        for neighbor in reversed(graph.get(current, [])):

            if neighbor not in visited:
                stack.append(neighbor)

    nodes_visited = len(visited)

    return order, nodes_visited