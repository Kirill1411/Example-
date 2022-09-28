def get_input():
    number_a = input("Enter number: ")
    equation = input("Enter equation: ")
    number_b = input("Enter number: ")
    numbers = number_a + ' ' + equation + ' ' + number_b
    return numbers


def send_info(a):
    print(f'Your result: {a}')