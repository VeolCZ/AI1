# The set of variables of the CSP with domains
from CSP_solver import CSP, Constraint, Variable, all_diff

variables = [
    Variable("U", domain=[*range(1, 10)]),
    Variable("N", domain=[*range(1, 10)]),
    Variable("O", domain=[*range(1, 10)]),
    Variable("E", domain=[*range(0, 10)]),
    Variable("Z", domain=[*range(0, 10)]),
    Variable("F", domain=[*range(0, 10)]),
]

# Here are the constraints:
constraints = all_diff(variables) + [
    Constraint(
        "(U*10+N + U*10+N + N*10**3+E*10**2+U*10+F) == (O*10**3+N*10**2+Z*10+E)",
    ),
]

# construct a csp with the variables and constraints
csp = CSP(
    variables,
    constraints,
    init_node=True,
    init_arc=True,
    keep_node=True,
    keep_arc=True,
    heuristic="mrv",
)

# Solve the csp and use verbose = True in order to print the search tree
csp.solve(verbose=False)
