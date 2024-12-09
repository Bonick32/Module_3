
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

def calculate_structure_sum(lists):

    for i in lists:
        if isinstance(i, int):
            flat_list_.append(i)
        if isinstance(i, str):
            flat_list_.append(len(i))

        if isinstance(i, dict):             # так как у нас в примере пара "Ключ: значение" это "строка: число"
            values_ = list(i.values())      # то я не стал усложнять распаковку словаря проверкой на тип
            for jv in values_:              # ключа и значения, иначе добавил бы в виде, приведенном выше,
                flat_list_.append(jv)       # увеличивая код. Вывести в отдельную функцию - пока не разобрался, как
            keys_ = list(i.keys())
            for jk in keys_:
                flat_list_.append(len(jk))

        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            calculate_structure_sum(i)
    return sum(flat_list_)

result = calculate_structure_sum(data_structure)
print(result)