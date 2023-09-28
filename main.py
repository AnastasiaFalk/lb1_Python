import math  # імпортування модуля math для виконання математичних операцій

# задання двох векторів як списки цілих чисел
v1 = [1, 7, 4, 4, 7]
v2 = [1, -9, 2, 0, 4]

def vector_length(vector): # функція для обчислення довжини вектора
    sum_of_squares = sum([x ** 2 for x in vector]) # обчислення суми квадратів елементів вектора
    length = math.sqrt(sum_of_squares) # корінь для отримання довжини
    return length

def addition_possibility(v1, v2): # функція для перевірки можливості додавання векторів
    return len(v1) == len(v2)

def subtraction_possibility(v1, v2): # функція для перевірки можливості віднімання векторів
    return len(v1) == len(v2)

def scalar_product_possibility(v1, v2): # функція для перевірки можливості скалярного добутку двох векторів
    return len(v1) == len(v2)

def v_addition(v1, v2): # функція додавання двох векторів
    if addition_possibility(v1, v2): # перевірка умови
        result = [x + y for x, y in zip(v1, v2)] # обчислення у випадку виконання
        return result # повернення результату обчислення
    else: # у випадку невиконання
        return "Додавання векторів неможливе через різні розмірності." # виведення тексту у випадку невиконання умови

def v_subtraction(v1, v2): # функція віднімання двох векторів
    if subtraction_possibility(v1, v2):
        result = [x - y for x, y in zip(v1, v2)]
        return result
    else:
        return "Віднімання векторів неможливе через різні розмірності."

def scalar_product(v1, v2): # функція обчислення скалярного добутку двох векторів
    if scalar_product_possibility(v1, v2):
        result = sum([x * y for x, y in zip(v1, v2)])
        return result
    else:
        return "Скалярний добуток неможливий через різні розмірності."

length_of_v1 = vector_length(v1) # обчислення довжини першого вектора
print("Довжина першого вектора:", length_of_v1)

length_of_v2 = vector_length(v2) # обчислення довжини другого вектора
print("Довжина другого вектора:", length_of_v2)

result_addition = v_addition(v1, v2) # додавання векторів
print("Додавання векторів:", result_addition)

result_subtraction = v_subtraction(v1, v2) # віднімання векторів
print("Віднімання векторів:", result_subtraction)

result_scalar_product = scalar_product(v1, v2) # скалярний добуток двох векторів
print("Скалярний добуток:", result_scalar_product)
