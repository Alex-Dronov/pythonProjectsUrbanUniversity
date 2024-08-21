my_dict = {1:'First', 2:'Second', 3:'Third'}
print(type(my_dict))
print("Dictionary:", my_dict)
print("Existing value:", my_dict[2])
key_ = 5
print(my_dict.get(key_, 'The dictionary does not contain a pair with the key: ' + str(key_)))
my_dict.update({5:'Fifth', 4:'Fourth'})
deleted_value = my_dict.pop(2)
print('Deleted value:', deleted_value)
print('Modified dictionary:', my_dict)
print()

my_set = {'223 - 322', 'Звоните в любое время', 2, 2, 3, 3, 2, 2, True, 'OR', False, 'True'}
print('Set: ', my_set)
my_set.add((223, 322))
my_set.add(223)
my_set.discard('Звоните в любое время')
print('Modified set: ', my_set)