first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [ len(st_) for st_ in first_strings if len(st_) > 5 ]
second_result = [ (f_st, s_st) for f_st in first_strings for s_st in second_strings if len(f_st) == len(s_st) ]
third_result = { st_ : len(st_) for st_ in (first_strings + second_strings) if not len(st_) % 2 }

print(first_result)
print(second_result)
print(third_result)