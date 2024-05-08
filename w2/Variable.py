from w2.Constraint import Constraint


class Variable:

    def __init__(self, name, domain):
        # variable name as string
        self.name = name

        # variables domain as list
        self.domain = domain

        # the variables values, as assigned by the solver
        self.value = None

        # The constraints the variable is involved in (Will be assigned later)
        self.constraints = []

    # checks if after assigning value d there exist a legal value for the
    # other variable w.r.t the  binary-constraint
    def exists_legal(self, d, other, binary_constraint) -> bool:

        is_legal = False
        self.value = d
        for d_other in other.domain:
            other.value = d_other
            if binary_constraint.evaluate():
                is_legal = True
                break

        # reverse value changes
        other.value = None
        self.value = None
        return is_legal

    # returns all constraints the variable is involved in with a given number of unassigned variables
    def constraints_with_degree(self, n_unassigned) -> list[Constraint]:
        return [
            c for c in self.constraints if c.n_unassigned_variables() == n_unassigned
        ]

    # checks if the variable is involved in a fully assigned constraint that evaluated to False.
    def is_conflicting(self) -> bool:
        fully_assigned_constraints = self.constraints_with_degree(n_unassigned=0)
        for constraint in fully_assigned_constraints:
            if not constraint.evaluate():
                return True
        return False
