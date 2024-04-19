
def main(input_str: str) -> str:
    try:
        tokens = input_str.split()
        if len(tokens) !=3:
            raise ValueError('Неверный формат ввода')

        a, operator, b = tokens
        a = int(a)
        b = int(b)

        if not ( 1 <= a <= 10 ) or not ( 1 <= b <=10 ):
            raise  ValueError('Допустимый диапазон вводимых чисел 1 - 10.')

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a // b
        else:
            raise ValueError('Недопустимый оператор')
        return str(result)
    except ValueError as ve:
        raise ve

while True:
    try:
        user_str = input()
        print(main(user_str))
    except ValueError as ve:
        print(ve)
        break




