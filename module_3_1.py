calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string = ''):

    count_calls()

    tuple_ = len(string), string.upper(),string.lower()
    return tuple_

def is_contains (list_to_search, string = ''):

    count_calls()

    if list_to_search is None:
        list_to_search = []

    string = string.lower()
    is_contains_ = False

    for str_ in list_to_search:
        if str(str_).lower() == string:
            is_contains_ = True
        else:
            is_contains_ = False

    return is_contains_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains(['ban', 'BaNaN', 'urBAN'], 'Urban')) # Urban ~ urBAN
print(is_contains(['recycling', 'cyclic'], 'cycle')) # No matches
print(calls)