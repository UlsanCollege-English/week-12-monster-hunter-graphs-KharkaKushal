# src/challenges.py

from collections import defaultdict


def build_hunter_map(edges):
    """
    Build an undirected graph from edge pairs.

    Returns:
        dict[str, list[str]]
    """
    graph = defaultdict(set)

    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    return {node: list(neighbors) for node, neighbors in graph.items()}


def build_weighted_hunter_map(edges):
    """
    Build an undirected weighted graph.

    Keeps the lowest weight for duplicate edges.
    Raises ValueError for non-positive weights.
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


def map_summary(graph):
    """
    Return number of locations and undirected routes.
    """
    locations = len(graph)

    total_edges = sum(len(neighbors) for neighbors in graph.values())
    routes = total_edges // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph):
    """
    Return the location with the highest degree.
    Ties are resolved alphabetically.
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


def priority_hunt_order(reports):
    """
    Sort by priority ascending, then alphabetically.
    Returns only location names.
    """
    sorted_reports = sorted(reports, key=lambda x: (x[0], x[1]))

    return [location for _, location in sorted_reports]