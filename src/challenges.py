"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs.

    Each tuple represents a two-way route between two monster sighting
    locations.

    Args:
        edges: A list of route pairs, such as
            [("Old Theater", "Train Station")].

    Returns:
        A dictionary where each key is a location and each value is a list
        of neighboring locations.

    Rules:
        - Add both directions for each route.
        - Include every location that appears in the input.
        - Do not duplicate neighbors if the same route appears more than once.
    """
    graph: dict[str, set[str]] = {}

    for a, b in edges:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    return {location: sorted(neighbors) for location, neighbors in graph.items()}


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples.

    Each tuple represents a two-way route with a positive danger score.

    Args:
        edges: A list of route triples, such as
            [("Old Theater", "Train Station", 4)].

    Returns:
        A nested dictionary where graph[start][end] is the danger score.

    Rules:
        - Add both directions for each route.
        - Danger scores must be positive integers.
        - If danger score is 0 or negative, raise ValueError.
        - If the same route appears more than once, keep the lowest score.
    """
    graph: dict[str, dict[str, int]] = {}

    for a, b, score in edges:
        if score <= 0:
            raise ValueError("Danger scores must be positive integers.")

        graph.setdefault(a, {})
        graph.setdefault(b, {})

        current_ab = graph[a].get(b)
        current_ba = graph[b].get(a)

        if current_ab is None or score < current_ab:
            graph[a][b] = score

        if current_ba is None or score < current_ba:
            graph[b][a] = score

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes.

    Args:
        graph: An undirected adjacency list.

    Returns:
        A dictionary with:
            - "locations": number of locations
            - "routes": number of undirected routes

    Example:
        {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["A"],
        }

        returns {"locations": 3, "routes": 2}
    """
    locations = len(graph)
    routes = sum(len(neighbors) for neighbors in graph.values()) // 2

    return {"locations": locations, "routes": routes}


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors.

    Args:
        graph: An undirected adjacency list.

    Returns:
        The location with the most neighbors.
        If the graph is empty, return None.
        If there is a tie, return the alphabetically first location.
    """
    if not graph:
        return None

    return min(
        graph,
        key=lambda location: (-len(graph[location]), location),
    )


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent.

    Lower priority number means more urgent.

    Args:
        reports: A list of tuples in the form (priority, location).

    Returns:
        A list of locations ordered from lowest priority number to highest.

    Requirement:
        Use heapq.
    """
    heap: list[tuple[int, str]] = []

    for priority, location in reports:
        heapq.heappush(heap, (priority, location))

    ordered: list[str] = []

    while heap:
        _, location = heapq.heappop(heap)
        ordered.append(location)

    return ordered