import ast


# does not work for variables that include square brackets
def connect_variables_and_constraints(csp):
    name_variable_map = dict()
    for variable in csp.variables:
        name_variable_map[variable.name] = variable

    warnings = []

    for c in csp.constraints:
        # print(c.equation)
        parsed = ast.parse(c.equation)
        for elt in ast.walk(parsed):
            if isinstance(elt, ast.Name):
                var_name = elt.id
                try:
                    var = name_variable_map[var_name]
                except KeyError:
                    if var_name not in warnings:
                        print(
                            f"Warning: variable '{var_name}' not recognized. Will be interpreted as a constant or function."
                        )
                        warnings.append(var_name)
                    continue
                if var not in c.variables:
                    c.variables.append(var)
                    var.constraints.append(c)
