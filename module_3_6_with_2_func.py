
#data_structure = [
#    [1, 2, 3],
#    {'a': 4, 'b': 5},
#    (6, {'cube': 7, 'drum': 8}),
#    "Hello",
#    ((), [{(2, 'Urban', ('Urban2', 35))}]),
#    {'s':(1, 1), 'a':{'sz': 1}}  # не знаю почему, но здесь не считает значение 1 в словаре, находящимся в словаре 
#]
#
#flat_list_ = [] # К сожалению, не смог найти решение без создания плоского списка,
                # состоящего из всех чисел и длин строк, в том числе ключей словаря.
                # Чувствую, что я где-то рядом с более лучшим решением, но не нашел,
                # как сделать запись типа i + calculate_structure_sum(i)
#def check_and_past(value_, list_flat):
#    
#    if isinstance(value_, int):
#        list_flat.append(value_)
#    if isinstance(value_, str):
#        list_flat.append(len(value_))
#
#def calculate_structure_sum(lists):
#
#    for i in lists:
#        check_and_past(i, flat_list_)
#            
#        if isinstance(i, dict):             
#            values_ = list(i.values())      
#            for jv in values_: 
#                if isinstance(jv, int) or isinstance(jv, str):
#                    check_and_past(jv, flat_list_) 
#
#                if isinstance(jv, list) or isinstance(jv, tuple) or isinstance(jv, set):
#                    calculate_structure_sum(jv)
#                if isinstance(jv, dict):
#                    calculate_structure_sum(jv)
#    
#            keys_ = list(i.keys())
#            for jk in keys_:
#                check_and_past(jk, flat_list_)
#
#        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
#            calculate_structure_sum(i)
#    return sum(flat_list_)
#
#result = calculate_structure_sum(data_structure)
#print(result)

# после вебинара переделал, как в примере... а в своем ночью разберусь
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': {'x': 2, 'n': 3} , 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(lists):
    summa = 0
    for i in lists:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)

        elif isinstance(i, dict):             # так как у нас в примере пара "Ключ: значение" это "строка: число"
            summa += calculate_structure_sum(i.items())

        elif isinstance(i, (list, tuple, set)):
            summa += calculate_structure_sum(i)
    return summa

result = calculate_structure_sum(data_structure)
print(result)
