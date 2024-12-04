def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])


    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if len(str_number) == 1:
        if first == 0:  # хоть в условии и не прописано, но из примера (40203) ясно, что 0 нужно не учитывать, чтоб
            first = 1   # перемножить цифры, из которых состоит число. Единица на результат не влияет
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
