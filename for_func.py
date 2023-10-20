import csv
import ast

def extract_function_data(code):
    result = []
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            params = ', '.join(arg.arg for arg in node.args.args)
            body = [line.rstrip() for line in ast.get_source_segment(code, node).split('\n')[1:]]
            result.append((func_name, params, body))

    return result

# Функция для чтения таблицы из файла CSV
def read_table(file_path):
    table = []
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    return table

# Функция для записи таблицы в файл CSV
def write_table(table, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(table)

# Функция для чтения записи из таблицы
def read_record(table, index):
    if 0 <= index < len(table):
        return table[index]
    else:
        return None

# Функция для записи записи в таблицу
def write_record(table, record):
    table.append(record)

# Функция для редактирования записи в таблице
def edit_record(table, index, column_index, new_value):
    if 0 <= index < len(table) and 0 <= column_index < len(table[index]):
        table[index][column_index] = new_value

# Функция для удаления записи из таблицы
def delete_record(table, index):
    if 0 <= index < len(table):
        del table[index]

# Функция для поиска записей в таблице по ключевому слову
def search_records(table, keyword):
    results = []
    for record in table:
        for value in record:
            if keyword in value:
                results.append(record)
                break
    return results

def write_function_data(function_data, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Function Name", "Parameters", "Body"])
        for func_name, params, body in function_data:
            writer.writerow([func_name, params, "\n".join(body)])



