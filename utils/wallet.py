import random, string
from database.db import get_user

def generate_wallet():
    return "F" + ''.join(random.choices(string.ascii_letters + string.digits, k=33))

def get_or_create_wallet(user_id):
    user = get_user(user_id)
    if user:
        return user[1]
    return generate_wallet()