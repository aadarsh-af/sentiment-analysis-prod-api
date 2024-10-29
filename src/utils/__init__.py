import time
from functools import wraps


def time_spent(func):
    """
    A decorator function to calculate the total time spent by any function to execute.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Function `{func.__name__}` was executed in {total_time:.4f} seconds.")
        return result

    return wrapper
