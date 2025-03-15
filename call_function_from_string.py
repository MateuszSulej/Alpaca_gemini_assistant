def call_function_from_string(class_, function_string):
    array = get_array(function_string)
    name_of_function = array[0]
    arguments_arr = array[1:]

    arguments_arr = [int(arg) if arg.isdigit() else arg for arg in arguments_arr]

    if hasattr(class_, name_of_function):
        func = getattr(class_, name_of_function)
        if len(arguments_arr) > 0 and arguments_arr[0] != '':
            print(func(*arguments_arr))
            print("Function done")
        else:
            print(func())
    else:
        print("Function not found!")


def get_array(function_string):
    function_string = function_string[:-1]

    array_output = []
    while len(function_string) > 1:
        try:
            str1, function_string = function_string.split(",", 1)
        except Exception:
            break
        array_output.append(str1)

    array_output.append(function_string)

    return array_output