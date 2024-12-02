def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()               # получил > 1 string True
print_params(78, '54')          # получил > 78 54 True
print_params(a = 4)          # получил > 4 string True
print_params(b = 25)         # получил > 1 25 True
print_params(c = [1, 2, 3])  # получил > 1 string [1, 2, 3]

values_list = [854, False, 'Why not']
values_dict = {'a' : 'int', 'b' : 64, 'c' : 79}

print_params(*values_list)  # получил > 854 False Why not
print_params(**values_dict) # получил > int 64 79

values_list_2 = [54.765, 'STRING']
print_params(*values_list_2, 42) # получил > 54.765 STRING 42

def append_to_list(item, list_my = None):
    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)

append_to_list(1) # получил > [1]
append_to_list(2) # получил > [2]


def append_to_list_wrong(item, list_my = []):
        list_my.append(item)
        print(list_my)

append_to_list_wrong(1) # получил > [1]
append_to_list_wrong(2) # получил > [1, 2]