
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

flat_list_ = [] # К сожалению, не смог найти решение без создания плоского списка,
                # состоящего из всех чисел и длин строк, в том числе ключей словаря.
                # Чувствую, что я где-то рядом с более лучшим решением, но не нашел,
                # как сделать запись типа i + calculate_structure_sum(i)
def check_and_past(value_, list_data, list_flat):
    
    if isinstance(value_, int):
        list_flat.append(value_)
    if isinstance(value_, str):
        list_flat.append(len(value_))

def calculate_structure_sum(lists):

    for i in lists:
        check_and_past(i, lists, flat_list_)
            
        

        if isinstance(i, dict):             
            values_ = list(i.values())      
            for jv in values_:              
                check_and_past(jv, values_, flat_list_)      
            keys_ = list(i.keys())
            for jk in keys_:
                check_and_past(jk, keys_, flat_list_)

        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            calculate_structure_sum(i)
    return sum(flat_list_)

result = calculate_structure_sum(data_structure)
print(result)