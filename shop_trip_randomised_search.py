import six
import sys

sys.modules[
    "sklearn.externals.six"
] = six
import mlrose
import numpy as np

# Create list of shop coordinates
shop_coords = [
    (1, 1),
    (1, 3),
    (3, 6),
    (3, 4),
    (6, 7),
    (5, 5),
    (6, 3),
    (7, 2),
    (5, 3),
]

problem_fit = mlrose.TSPOpt(
    length=9,
    coords=shop_coords,
    maximize=False,
)

(
    best_route,
    best_fitness,
) = mlrose.genetic_alg(
    problem_fit,
    mutation_prob=0.2,
    max_attempts=100,
    random_state=2,
)

print(
    "The best route found is: ",
    best_route,
)

print(
    "The fitness at the best route is: ",
    best_fitness,
)
