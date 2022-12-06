"""
"""
from random import randint


class Calculate:

    def __init__(self: object, difficulty: int) -> None:
        self.__difficulty: int = difficulty
        self.__value1: int = self.generate_numbers
        self.__value2: int = self.generate_numbers
        self.__value3: int = self.generate_numbers
        self.__operation = randint(1, 3)  # If 1 == soma, If 2 == minus, if 3 == multiply
        self.__result = self.generate_result

    @property
    def difficulty(self: object) -> int:
        return self.__difficulty

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def value3(self: object) -> int:
        return self.__value3

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Soma'
        elif self.operation == 2:
            op = 'Minus'
        elif self.operation == 3:
            op = 'Multiply'
        else:
            op = 'Invalid operation'
        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nValue 3: {self.value3} \nDifficulty: {self.difficulty} \nOperation: {op}'

    @property
    def generate_numbers(self: object) -> int:
        if self.difficulty == 1:
            return randint(1, 10)
        elif self.difficulty == 2:
            return randint(1, 100)
        elif self.difficulty == 3:
            return randint(100, 1000)
        else:
            return randint(0, 10000)

    @property
    def generate_result(self: object) -> int:
        if self.operation == 1:  # soma
            return self.value1 + self.value2 + self.value3
        elif self.operation == 2:  # minus
            return self.value1 - self.value2 - self.value3
        elif self.operation == 3:  # multiply
            return self.value1 * self.value2 * self.value3

    @property
    def _op_symbol(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def check_result(self: object, answer: int) -> bool:
        right: bool = False

        if self.result == answer:
            print('Right answer!')
            right = True
        else:
            print('Wrong answer!')
        print(f'{self.value1} {self._op_symbol} {self.value2} {self._op_symbol} {self.value3} = {self.result}')
        return right

    def show_operation(self: object) -> None:
        print(f'{self.value1} {self._op_symbol} {self.value2} {self._op_symbol} {self.value3}')


