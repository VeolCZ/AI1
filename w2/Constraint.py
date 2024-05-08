from w2.Variable import Variable


class Constraint:
    def __init__(self, equation):
        # The equation as string
        self.equation = equation

        # The variables of the constraint (Will be assigned later)
        self.variables = []

        # The csp class (Will be assigned later)
        self.csp = None

    def n_variables(self) -> int:
        return len(self.variables)

    def n_unassigned_variables(self) -> int:
        c = 0
        for v in self.variables:
            if v.value is None:
                c += 1
        return c

    def unassigned_variables(self) -> list[Variable]:
        return [v for v in self.variables if v.value is None]

    def evaluate(self):
        self.csp.n_constraints_evaluated += 1
        values = dict()
        for variable in self.variables:
            values[variable.name] = variable.value
        return eval(self.equation, {}, values)
