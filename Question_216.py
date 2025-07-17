def read_file(name):
    try:
        file = open(name, 'r')
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print(f'Error: File {name} not found.')
        return None
