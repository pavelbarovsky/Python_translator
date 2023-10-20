import for_func as ff
import for_varable as fv

source_code = """
import numpy as np

def calculate_distance(point1, point2):
    # Вычисление расстояния между двумя точками
    distance = np.linalg.norm(np.array(point1) - np.array(point2))
    return distance

def find_nearest_point(start_point, control_points):
    # Поиск ближайшей точки к текущей точке
    min_distance = float('inf')
    nearest_point = None

    for point in control_points:
        distance = calculate_distance(point, start_point)
        if distance < min_distance:
            min_distance = distance
            nearest_point = point

    return nearest_point

def move_robot(start_point, nearest_point):
    # Код для движения робота
    print(f"Moving robot from {start_point} to {nearest_point}")

def find_path(start_point, control_points):
    path = []

    while len(control_points) > 0:
        nearest_point = find_nearest_point(start_point, control_points)
        path.append(nearest_point)
        start_point = nearest_point
        control_points.remove(nearest_point)

        move_robot(start_point, nearest_point)

    return path

start_point = [0, 0]
control_points = [[2, 4], [4, 7], [1, 3], [10, 8]]

path = find_path(start_point, control_points)

print("Path:")
for point in path:
    print(point)
"""

function_data = ff.extract_function_data(source_code)
variables, values = fv.extract_variables(source_code)

ff.write_function_data(function_data, "function_data.csv")
fv.write_variables_to_csv(variables, values, "variable_data.csv")

# работа с таблицей функций

# Чтение таблицы из файла CSV
table = ff.read_table("function_data.csv")
print("Чтение таблицы:")
print(table, '\n')

# Чтение записи
record = ff.read_record(table, 0)
print("Чтение записи:", '\n', record, '\n')
# print(record)

# Запись новой записи
new_record = ["new_function", "new_params", "new_body"]
ff.write_record(table, new_record)

# Редактирование записи
ff.edit_record(table, 2, 2, "print('hello world!')")

# Удаление записи
ff.delete_record(table, 1)

# Поиск записей по ключевому слову
keyword_1 = "robot"
results = ff.search_records(table, keyword_1)
print(f"Результат поиска в csv файле функций по ключевому слову '{keyword_1}':")
for record in results:
    print(record)

# Запись измененной таблицы в новый файл CSV
ff.write_table(table, "modified_function_data.csv")

# работа с таблицей переменных

# Чтение и вывод исходной таблицы п
header, table = fv.read_table_var("variable_data.csv")
print("Чтение таблицы:")
print(table, '\n')

# Добавление новой записи в таблицу
new_record = ["new_variable", "new_value"]
table.append(new_record)

# Запись таблицы в новый CSV-файл
fv.write_table_var(header, table, "new_variable_data.csv")

# Чтение и вывод записи по индексу
header, record = fv.read_record_var("new_variable_data.csv", 1)
print(f"Чтение записи:")
print(header, '\n', record, '\n')

# Редактирование значения столбца в записи
new_value = "None"
fv.edit_record_var("new_variable_data.csv", 0, 1, new_value)

# Удаление записи
fv.delete_record_var("new_variable_data.csv", 4)

# Поиск записей по ключевому слову
keyword_2 = "path"
header, results = fv.search_records_var("new_variable_data.csv", keyword_2)
print(f"Результаты поиска для ключевого слова '{keyword_2}':")
print(header)
for index, row in results:
    print(f"Запись {index}: {row}")