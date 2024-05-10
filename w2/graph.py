# The set of variables of the CSP with domains
from CSP_solver import CSP, Constraint, Variable

variables = [
    Variable("A", domain=[1, 2, 3, 4]),
    Variable("B", domain=[1, 2, 3, 4]),
    Variable("C", domain=[1, 2, 3, 4]),
    Variable("D", domain=[1, 2, 3, 4]),
    Variable("E", domain=[1, 2, 3, 4]),
]

# Here are the constraints:
constraints = [
    Constraint("A > D"),
    Constraint("B >= A"),
    Constraint("B != C"),
    Constraint("C != A"),
    Constraint("C != (D + 1)"),
    Constraint("C != D"),
    Constraint("D > E"),
    Constraint("C > E"),
    Constraint("B != C"),
]

# construct a csp with the variables and constraints
csp = CSP(
    variables,
    constraints,
    init_node=False,
    init_arc=False,
    keep_node=False,
    keep_arc=False,
    heuristic="deg",
)

# Solve the csp and use verbose = True in order to print the search tree
csp.solve(verbose=False)
