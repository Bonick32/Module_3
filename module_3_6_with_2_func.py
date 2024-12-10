data_structure = [
   [1, 2, 3],
   {'a': 4, 'b': 5},
   (6, {'cube': 7, 'drum': 8}),
   "Hello",
   ((), [{(2, 'Urban', ('Urban2', 35))}]),
   {'s':(1, 1), 'a':{'sz': 1}}  # 99 + 7
]

flat_list_ = []

def check_and_past(value_, list_flat):
   if isinstance(value_, (int, float)):
       list_flat.append(value_)
   if isinstance(value_, str):
       list_flat.append(len(value_))

def calculate_structure_sum(lists):
   for i in lists:
       check_and_past(i, flat_list_)
       if isinstance(i, dict):
           items = list(i.items())
           calculate_structure_sum(items)
       elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
           calculate_structure_sum(i)
   return sum(flat_list_)

result = calculate_structure_sum(data_structure)
print(result)

# после вебинара переделал без списка и без функции 

# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': {'x': 2, 'n': 3} , 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}]) # 99
# ]
#
#
# def calculate_structure_sum(lists):
#     summa = 0
#     for i in lists:
#         if isinstance(i, (int, float)):
#             summa += i
#         elif isinstance(i, str):
#             summa += len(i)
#
#         elif isinstance(i, dict):          
#             summa += calculate_structure_sum(i.items())
#
#         elif isinstance(i, (list, tuple, set)):
#             summa += calculate_structure_sum(i)
#     return summa
#
# result = calculate_structure_sum(data_structure)
# print(result)

result = calculate_structure_sum(data_structure)
print(result)
