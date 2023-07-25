def square(x):
    return x**2

# call a function that call another function
def my_map(func, input_list):
    out_list = []

    for item in input_list:
        out_list.append(func(item))

    return out_list



input_list = [1, 2, 3, 4]

result = my_map(square, input_list)
