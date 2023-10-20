import csv
import ast

def extract_variables(source_code):
    tree = ast.parse(source_code)
    variables = []
    values = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.targets[0], ast.Name):
                variable_name = node.targets[0].id
                value = ast.unparse(node.value)
                variables.append(variable_name)
                values.append(value)

    return variables, values

def write_variables_to_csv(variables, values, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Variable Name", "Value"])
        for variable, value in zip(variables, values):
            writer.writerow([variable, str(value)])

def read_table_var(file_path):
    table = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            table.append(row)
    return header, table

def write_table_var(header, data, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def read_record_var(file_path, record_index):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = None
        for i, row in enumerate(reader):
            if i == record_index:
                data = row
                break
    return header, data

def edit_record_var(file_path, record_index, column_index, new_value):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows[record_index + 1][column_index] = new_value
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def delete_record_var(file_path, record_index):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        del rows[record_index + 1]
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def search_records_var(file_path, keyword):
    results = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for i, row in enumerate(reader):
            for value in row:
                if keyword in value:
                    results.append((i, row))
                    break
    return header, results