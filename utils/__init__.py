import os

def impute_value(value):
    if value == "":
        return None
    return value.replace("\n", "")


def cast_value(value, cast_func):
    if value is None:
        return None
    return eval(cast_func)(value)


def deserialize(row):
    imputed_values = list(map(impute_value, row.split(",")))
    cast_dict = {
        "bool": [2, -1, 6],
        "float": [5] + list(range(7, 12)),
    }
    for key in cast_dict.keys():
        indxs = cast_dict[key]
        for ind in indxs:
            imputed_values[ind] = cast_value(imputed_values[ind], key)

    return imputed_values


def get_data():
    path = os.path.join(os.path.dirname(__file__), 'data.csv')
    with open(path) as data_file:
        next(data_file)

        return [deserialize(line) for line in data_file]