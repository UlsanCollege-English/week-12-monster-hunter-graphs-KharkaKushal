[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/80z-ZS6n)
# Week 12: Monster Hunter Graphs

## Student

Name: Kharka Kushal

Student ID: TBD

## Summary

This assignment implements graph data structures to represent a monster activity network across a city. The graph uses an undirected adjacency list to store locations (nodes) and routes (edges), with optional danger scores for weighted graphs. The implementation provides functions to build graphs, analyze their structure, and prioritize monster hunting tasks. The most complex function was determining the most connected location while resolving ties alphabetically.

## Approach

- `build_hunter_map`: Creates an undirected adjacency list using `defaultdict(set)` to automatically handle bidirectional edges and avoid duplicate neighbors.
- `build_weighted_hunter_map`: Similar structure but stores danger scores as dictionary values, keeping the minimum score when duplicates exist and validating positive weights.
- `map_summary`: Counts unique locations (keys) and divides total neighbor connections by 2 to get undirected route count.
- `most_connected_location`: Finds the maximum degree (neighbor count), identifies all nodes with that degree, and returns the alphabetically first one.
- `priority_hunt_order`: Uses `heapq` to efficiently extract sightings in priority order, automatically handling both priority and alphabetical tie-breaking.

## Complexity

### `build_hunter_map`

- Time: O(E) where E is the number of edges
- Space: O(V + E) where V is the number of locations
- Why: Each edge is processed once. Space stores all vertices and edges in adjacency list.

### `build_weighted_hunter_map`

- Time: O(E) where E is the number of edges
- Space: O(V + E) where V is the number of locations
- Why: Each edge is processed once with O(1) weight comparison. Space stores all vertices and weighted edges.

### `map_summary`

- Time: O(V + E) where V is vertices and E is total edges
- Space: O(1) excluding input
- Why: Must iterate through all locations and neighbors to count routes.

### `most_connected_location`

- Time: O(V) where V is number of locations
- Space: O(V) for storing candidates list in worst case
- Why: Must examine all locations to find max degree, then sort candidates alphabetically.

### `priority_hunt_order`

- Time: O(R log R) where R is number of reports
- Space: O(R) for heap storage
- Why: Building heap is O(R log R), extraction is O(R log R). Space proportional to reports.

## Edge-Case Checklist

- [x] Empty graphs return appropriate values (empty dict, 0 locations/routes, None for most connected)
- [x] Single location graphs work correctly (one node, zero routes)
- [x] Duplicate edges are handled (takes minimum weight, no duplicate neighbors)
- [x] Negative/zero weights are rejected with ValueError
- [x] Alphabetical tie-breaking works in both `most_connected_location` and `priority_hunt_order`
- [x] Empty reports list returns empty result list

## Assistance & Sources

- Python `collections.defaultdict` documentation for efficient graph building
- `heapq` module documentation for priority queue implementation
- Assignment requirements and test cases provided in HOMEWORK_BRIEF.md

- Why:

### `map_summary`

- Time:
- Space:
- Why:

### `most_connected_location`

- Time:
- Space:
- Why:

### `priority_hunt_order`

- Time:
- Space:
- Why:

## Edge-Case Checklist

Check the cases you handled.

- [ ] Empty graph
- [ ] One route
- [ ] Duplicate routes
- [ ] Disconnected locations
- [ ] Tie for most connected location
- [ ] Positive weighted routes
- [ ] Invalid zero or negative danger score
- [ ] Empty priority report list

## Tests

Paste the result of your test run.

```bash
pytest -q
```

Result:

```text

```

## Assistance & Sources

AI used? Yes / No

If yes, what did it help with?

-

Other sources used:

-
