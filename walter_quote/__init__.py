import random

from .quotes import WALTER_QUOTES


def random_walter_quote() -> str:
    return random.choice(WALTER_QUOTES)
