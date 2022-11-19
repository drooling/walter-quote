import random

from .quotes import WALTER_QUOTES


def show_random_quote():
    print(random.choice(WALTER_QUOTES))


if __name__ == "__main__":
    show_random_quote()
