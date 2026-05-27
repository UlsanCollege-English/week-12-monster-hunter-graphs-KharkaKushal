# src/challenges.py

from collections import defaultdict
import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Build an undirected graph from edge pairs.

    Each route works both directions. Duplicate neighbors are not added.

    Args:
        edges: List of (location1, location2) tuples representing routes.

    Returns:
        dict[str, list[str]]: Adjacency list with all locations and neighbors.
    """
    graph = defaultdict(set)

    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    return {node: list(neighbors) for node, neighbors in graph.items()}


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """
    Build an undirected weighted graph from route triples.

    Keeps the lowest danger score for duplicate edges.
    Raises ValueError if any danger score is not positive.

    Args:
        edges: List of (location1, location2, danger_score) tuples.

    Returns:
        dict[str, dict[str, int]]: Weighted adjacency dict.

    Raises:
        ValueError: If any danger score is <= 0.
    """
    graph = defaultdict(dict)

    for a, b, weight in edges:
        if weight <= 0:
            raise ValueError("Weight must be positive")

        # Add/update a -> b
        if b not in graph[a] or weight < graph[a][b]:
            graph[a][b] = weight

        # Add/update b -> a
        if a not in graph[b] or weight < graph[b][a]:
            graph[b][a] = weight

    return dict(graph)


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """
    Return the number of locations and undirected routes in the graph.

    Args:
        graph: Adjacency list representation of the graph.

    Returns:
        dict[str, int]: Dictionary with 'locations' and 'routes' counts.
    """
    locations = len(graph)

    total_edges = sum(len(neighbors) for neighbors in graph.values())
    routes = total_edges // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """
    Return the location with the most neighbors (highest degree).

    Ties are resolved alphabetically (returns first alphabetically).

    Args:
        graph: Adjacency list representation of the graph.

    Returns:
        str | None: The most connected location, or None if graph is empty.
    """
    if not graph:
        return None

    max_degree = max(len(neighbors) for neighbors in graph.values())

    candidates = [
        location
        for location, neighbors in graph.items()
        if len(neighbors) == max_degree
    ]

    return sorted(candidates)[0]


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """
    Return monster sighting locations sorted by priority (urgent first).

    Lower priority number means more urgent.
    Uses heapq for efficient priority queue handling.
    Ties are resolved alphabetically.

    Args:
        reports: List of (priority, location) tuples.

    Returns:
        list[str]: Location names sorted from most urgent to least urgent.
    """
    heap = [(priority, location) for priority, location in reports]
    heapq.heapify(heap)

    result = []
    while heap:
        _, location = heapq.heappop(heap)
        result.append(location)

    return result