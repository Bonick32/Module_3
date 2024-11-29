calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    print(tuple_)

def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [s.lower() for s in list_to_search]
    if string.lower() in list_to_search:
        print(True)
    else:
        print(False)

string_info('Флегматик')
string_info('СаНгвинИк')
string_info('Synchrophasotron')

is_contains('Урбан', ['бан', 'БаНаН', 'урБАН'])
is_contains('цикл', ['цикличный', 'циклоп'])

print(calls)
