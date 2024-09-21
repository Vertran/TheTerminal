def read_custom_file(filepath):
    with open(filepath, 'r') as file:
        data = {}
        for line in file:
            if ':' in line:
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
        return data

# Example usage:
file_data = read_custom_file('image.vimg')
print(file_data)