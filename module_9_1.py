def apply_all_func(int_list, *functions):
    results = {}
    for fun_ in functions:
        results.__setitem__(fun_.__name__,fun_(int_list))

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
