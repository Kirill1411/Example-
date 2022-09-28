path = r'data.txt'
path_log = f'log.txt'


def get_info():
    with open(path, 'r') as data:
        data = data.read().split(' ')
    return data


def save_info(a):
    a = str(a)
    with open(path, 'w') as data:
        data.write(a)


def save_result(a):
    # a = str(a)
    with open(path, 'a') as data:
        data.write(f'\nYour result = {str(a)}')


def log(a, b):
    with open(path_log, 'a') as data:
        data.write('\nYour equation: {} {} {} = {}'.format(a[0], a[1], a[2], b))