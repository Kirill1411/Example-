import functions


def check(data):
    match data[1]:
        case '+':
            return functions.sum(data[0], data[2])
        case '-':
            return functions.minus(data[0], data[2])
        case '*':
            return functions.mult(data[0], data[2])
        case '/':
            return functions.dev(data[0], data[2])
        case _:
            print("Wrong equation sign!")
            return "Wrong equation sign!"