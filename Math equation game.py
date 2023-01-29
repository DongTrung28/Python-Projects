import random
import sys

def main():
    counter = 0
    score = 0

    choice = get_level()

    for _ in range(10):
        x = generate_integer(choice)
        for i in range(1):
            y = generate_integer(choice)

            answer = x + y
            question = input(f'{x} + {y} = ')

            if int(question) == answer:
                score += 1
            elif int(question) != answer:
                while True:
                    counter += 1
                    print("EEE")
                    question = input(f'{x} + {y} = ')
                    if counter == 2:
                        print("EEE")
                        print(f'{x} + {y} = ' + str(answer))
                        break

    result = "Score: " + str(score)
    print(result)

def get_level():
    levels = [1, 2, 3]
    level = input("Level: ")
    if level.isalpha() or int(level) <= 0 or int(level) > 3:
        input("Level: ")
    else:
        level = int(level)
        for j in levels:
            if level == j:
                return level


def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError



if __name__ == "__main__":
    main()
