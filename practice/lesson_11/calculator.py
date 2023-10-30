class CalculationExitException(Exception):
    pass


def input_int_number() -> int:
    while True:
        try:
            return int(input("Введите целое число: "))
        except ValueError as e:
            print('Ошибка:', e)
            print('Попробуйте снова')


def calculate(left: int, right: int, operation: str):
    match operation:
        case '!':
            raise CalculationExitException()
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case '/':
            return left / right
        case _:
            raise ValueError(f'Неподдерживаемая операция: {operation}')


def main():
    while True:
            a = input_int_number()
            b = input_int_number()
            operation = input('Введите операцию (введите ! для выхода): ')
            try:
                print(calculate(a, b, operation))
            except (ValueError, ZeroDivisionError) as e:
                print('Ошибка:', e)
            except CalculationExitException:
                print('Завершаем программу')
                break


if __name__ == '__main__':
    main()

