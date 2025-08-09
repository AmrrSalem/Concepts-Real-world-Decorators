"""
Example of using a decorator in Python.

Scenario:
    We want to measure how long certain functions take to execute.
    Instead of adding timing code to every function, we create a reusable decorator.

Why a decorator?
    - Adds functionality (timing) without changing the original function's code.
    - Can be applied to any function just by adding @time_it above it.
    - Keeps code DRY and clean.
"""

import time
from functools import wraps


def time_it(func):
    """
    A decorator that measures the execution time of the wrapped function.

    Args:
        func (callable): The function to wrap.

    Returns:
        callable: The wrapped function with timing capability.
    """
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        """
        Wrapper function that times the execution of 'func'.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed = end_time - start_time
        print(f"[TIMER] Function '{func.__name__}' took {elapsed:.4f} seconds.")
        return result

    return wrapper


@time_it
def slow_function():
    """
    Simulate a slow task.
    """
    time.sleep(1.5)
    print("Finished slow function.")


@time_it
def add_numbers(a, b):
    """
    Add two numbers with a simulated delay.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The sum of a and b.
    """
    time.sleep(0.5)
    return a + b


if __name__ == "__main__":
    slow_function()
    result = add_numbers(5, 7)
    print(f"Sum: {result}")
