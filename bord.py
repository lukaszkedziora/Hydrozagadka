def get_table_from_file(file_name):
    with open(file_name, 'r') as file:
        result = []
        for line in file:
            result.append(line)
        print(*result)
    return result