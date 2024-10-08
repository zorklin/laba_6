#індексація від 1
def func_f(input_list):
    p_list = [input_list[i] for i in range(len(input_list)) if i % 2 != 0]
    input_list.extend(p_list)
    return input_list

def func_s(input_list):
    return [item for item in set(input_list) if input_list.count(item) > 1]

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

list = [2, 3, 5, 12, 9, 11, 4]
result = func_f(list)
print(result)

result = func_s(list)
print(result)

x = set(range(8, 23))
y = {i for i in x if prime(i)}

print("Множина x:", x)
print("Множина y:", y)