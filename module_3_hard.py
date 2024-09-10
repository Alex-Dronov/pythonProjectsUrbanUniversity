def calculate_structure_sum(*args):

    sum_ = 0

    if isinstance(*args, list):
        list_of_args = list(*args)

        for i in list_of_args:
            sum_ += calculate_structure_sum(i)

    elif isinstance(*args, dict):
        list_of_args = dict(*args)

        for key, value in list_of_args.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)

    elif isinstance(*args, set):
        list_of_args = set(*args)

        for i in list_of_args:
            sum_ += calculate_structure_sum(i)

    elif isinstance(*args, tuple):
        list_of_args = tuple(*args)

        for i in list_of_args:
            sum_ += calculate_structure_sum(i)

    elif isinstance(*args, str):
        sum_ += len(*args)

    elif isinstance(*args, int):
        sum_ += int(*args)

    return sum_





data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)