# class Constraint(object):
#     pass

# class Variable(object):
#     pass


def add_to_dict(di, key, val):
    if di.get(key) is None:
        di[key] = [val]
    else:
        di[key].append(val)
