from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    difficulty: int = int(input('Inform the level of difficulty you want. Between 1 to 3:  '))

    calc = Calculate(difficulty)

    print('Inform the result of the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points = points + 1
        print(f'You have got {points} score points!')

    continuegame = int(input('Do you want to continue playing? 1 - Yes or 0 - No'))

    if continuegame:
        play(points)
    else:
        print(f'You have finished with {points} points!')
        print('See You Space CowBoy!')


if __name__ == '__main__':
    main()

