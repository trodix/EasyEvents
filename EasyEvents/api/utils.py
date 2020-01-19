import string
import random


def generate_ticket_number(size=8):
    return ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=size
        )
    )
