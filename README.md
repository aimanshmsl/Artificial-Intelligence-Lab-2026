# Airline Route Search: AI Lab 2026

This project explores classical graph-search algorithms using an airline network. It loads airport and route data, calculates great-circle distances, and compares Breadth-First Search (BFS), Depth-First Search (DFS), and Uniform-Cost Search (UCS) on sample airport-to-airport queries.

## What the project does

- Cleans airport and route records and builds a directed graph.
- Uses airport codes as graph nodes and airline routes as edges.
- Calculates route distances with the Haversine formula.
- Compares the paths, number of hops, total distance, search effort, and runtime returned by BFS, DFS, and UCS.
- Checks that every reported path uses real edges and that its distance matches the sum of those edges.
- Saves a route comparison plot and a CSV of metrics.

BFS finds a route with the fewest edges, while UCS minimizes total distance. DFS follows the graph's neighbor order and is included for comparison; its path is not guaranteed to be shortest.

## Repository layout

```text
.
├── all_datasets/
│   ├── lab01-03_airports.csv
│   └── lab01-03_routes.csv
├── all_experiments/
│   └── utils/
│       ├── core.py                       # BFS, DFS, and UCS implementations
│       ├── openflights.py                # Data cleaning and graph construction
│       ├── plotting.py                   # Route visualization
│       ├── search_queries.csv            # Example start and goal airports
│       └── lab01_search_foundations.py   # Lab 1 experiment
├── results/
│   └── lab01/
│       ├── metrics.csv
│       └── route_comparison.png
├── requirements.txt
└── test.py
```

## Requirements

- Python 3.10 or newer
- Packages listed in `requirements.txt`

## Setup

From the repository root, create and activate a virtual environment, then install the dependencies.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the experiment

Run the Lab 1 script from the repository root:

```bash
python all_experiments/utils/lab01_search_foundations.py
```

The script reads the CSV files in `all_datasets/` and writes updated outputs to `results/lab01/`:

- `metrics.csv` contains the paths and measurements for each algorithm and query.
- `route_comparison.png` visualizes the BFS, DFS, and UCS routes for query Q1 (KUL to KEF).

## Example results

The included results use these queries:

| Query | Start | Goal |
|---|---|---|
| Q1 | KUL | KEF |
| Q2 | SIN | EZE |
| Q3 | NRT | CPT |

For Q1, the saved results show BFS finding a 2-hop route, DFS finding a 23-hop route, and UCS finding a 4-hop route. UCS's route is shorter in total distance than the BFS route for this query, illustrating that the fewest flights and the shortest distance are different objectives.

## Notes

- The graph is directed: a route from airport A to airport B does not imply that a route from B to A exists.
- Search runtimes depend on the machine and may vary between runs.
- `test.py` currently contains a basic `hello world` placeholder; the experiment's path and cost checks run inside the Lab 1 script.
