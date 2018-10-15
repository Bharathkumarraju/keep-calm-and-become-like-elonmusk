from functools import wraps
from flask import session,Flask

def check_logging_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
# 1. Code to execute before calling the decorated function.
         if 'logged_in' in session:
# 2. Call the decorated function as required, returning its results if needed.
             return func(*args, **kwargs)
# 3. Code to execute INSTEAD of calling the decorated function
         return 'You are NOT logged in'
    return wrapper

