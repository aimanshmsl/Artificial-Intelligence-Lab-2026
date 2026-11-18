"""Genetic Algorithm for the fictional A-G delivery route problem."""
import random

# Reproducible experiment: the same seed produces the same run.
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Symmetric fictional distances in kilometres, supplied in the assignment.
DISTANCE = {
    "A": {"A": 0, "B": 4, "C": 8, "D": 6, "E": 7, "F": 9, "G": 5},
    "B": {"A": 4, "B": 0, "C": 5, "D": 7, "E": 3, "F": 8, "G": 6},
    "C": {"A": 8, "B": 5, "C": 0, "D": 4, "E": 6, "F": 3, "G": 7},
    "D": {"A": 6, "B": 7, "C": 4, "D": 0, "E": 5, "F": 6, "G": 8},
    "E": {"A": 7, "B": 3, "C": 6, "D": 5, "E": 0, "F": 4, "G": 6},
    "F": {"A": 9, "B": 8, "C": 3, "D": 6, "E": 4, "F": 0, "G": 5},
    "G": {"A": 5, "B": 6, "C": 7, "D": 8, "E": 6, "F": 5, "G": 0},
}
DEPOT = "A"
LOCATIONS = ["B", "C", "D", "E", "F", "G"]
POPULATION_SIZE = 100
GENERATIONS = 100
ELITE_COUNT = 2
MUTATION_RATE = 0.15
TOURNAMENT_SIZE = 4


def route_distance(chromosome):
    """Return the full closed-tour distance, including both depot legs."""
    route = [DEPOT] + chromosome + [DEPOT]
    return sum(DISTANCE[left][right] for left, right in zip(route, route[1:]))


def make_initial_population():
    """Each chromosome is a shuffled permutation of all delivery stops."""
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = LOCATIONS.copy()
        random.shuffle(chromosome)
        population.append(chromosome)
    return population


def select_parent(population):
    """Tournament selection favours shorter routes while retaining variety."""
    candidates = random.sample(population, TOURNAMENT_SIZE)
    return min(candidates, key=route_distance)


def order_crossover(parent_one, parent_two):
    """Order crossover (OX) preserves a permutation with no duplicate stops."""
    left, right = sorted(random.sample(range(len(parent_one)), 2))
    child = [None] * len(parent_one)
    child[left:right + 1] = parent_one[left:right + 1]
    parent_two_order = parent_two[right + 1:] + parent_two[:right + 1]
    remaining = [stop for stop in parent_two_order if stop not in child]
    fill_positions = list(range(right + 1, len(child))) + list(range(0, left))
    for position, stop in zip(fill_positions, remaining):
        child[position] = stop
    return child


def mutate(chromosome):
    """Swap two delivery stops; this keeps every location exactly once."""
    changed = chromosome.copy()
    if random.random() < MUTATION_RATE:
        first, second = random.sample(range(len(changed)), 2)
        changed[first], changed[second] = changed[second], changed[first]
    return changed


def run_genetic_algorithm():
    population = make_initial_population()
    for _ in range(GENERATIONS):
        population.sort(key=route_distance)
        next_generation = [route.copy() for route in population[:ELITE_COUNT]]
        while len(next_generation) < POPULATION_SIZE:
            parent_one = select_parent(population)
            parent_two = select_parent(population)
            child = order_crossover(parent_one, parent_two)
            next_generation.append(mutate(child))
        population = next_generation

    best = min(population, key=route_distance)
    return best, route_distance(best)


if __name__ == "__main__":
    best_chromosome, best_distance = run_genetic_algorithm()
    best_route = [DEPOT] + best_chromosome + [DEPOT]
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Generations: {GENERATIONS}")
    print(f"Best route: {' -> '.join(best_route)}")
    print(f"Total distance: {best_distance} km")


