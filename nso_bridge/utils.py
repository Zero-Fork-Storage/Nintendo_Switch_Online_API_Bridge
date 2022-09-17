import re


def is_friend_code(code):
    return re.match(r"/^\d{4}-\d{4}-\d{4}$/g", code)


def check_friend_code_hash(code):
    return re.match(r" /^[A-Za-z0-9]{10}$/;", code)


__all__ = [
    "is_friend_code",
    "check_friend_code_hash",
]
