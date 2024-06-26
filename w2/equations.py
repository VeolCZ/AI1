# The set of variables of the CSP with domains
from CSP_solver import CSP, Constraint, Variable

variables = [
    Variable("A", domain=[1, 2]),
    Variable("B", domain=[1, 2, 3]),
    Variable("C", domain=[1, 2, 3, 4]),
]

# Here are the constraints:
constraints = [Constraint("2 * A == C"), Constraint("A != B"), Constraint("A + B <= C")]

# construct a csp with the variables and constraints
csp = CSP(
    variables,
    constraints,
    init_node=False,
    init_arc=True,
    keep_node=True,
    keep_arc=True,
)

# Solve the csp and use verbose = True in order to print the search tree
csp.solve(verbose=True)
