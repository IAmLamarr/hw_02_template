def impute_value(value):
    if value == "":
        return None
    return value.replace("\n", "")


def cast_value(value, cast_func):
    if value is None:
        return None
    return eval(cast_func)(value)


def deserialise(row):
    imputed_values = list(map(impute_value, row.split(",")))
    cast_dict = {
        "bool": [2, -1, 6],
        "float": range(7, 10),
    }
    for key in cast_dict.keys():
        indxs = cast_dict[key]
        for ind in indxs:
            imputed_values[ind] = cast_value(imputed_values[ind], key)

    return imputed_values


def get_data():
    with open("./utils/data.csv") as data_file:
        next(data_file)

        return [deserialise(line) for line in data_file]