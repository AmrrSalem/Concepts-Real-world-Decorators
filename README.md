````markdown
# Python Decorator Example — Timing Function Execution

This example demonstrates how to use a **decorator** in Python to measure the execution time of functions without changing their core logic.

## What is a Decorator?

A **decorator** is a special function in Python that:
- Takes another function (or class) as input.
- Wraps it with extra behavior.
- Returns a new function with the original's behavior plus the new feature.

Decorators are often used for:
- Logging
- Timing execution
- Access control
- Caching
- Validation

## Scenario

We have multiple functions (`slow_function` and `add_numbers`) where we want to measure execution time.

Instead of adding timing code to each function separately, we create a `time_it` decorator and apply it using the `@` syntax.

## Benefits of Using a Decorator

- **Keeps code DRY** — no repetition of timing logic.
- **Reusable** — can be applied to any function by adding `@time_it`.
- **Clean separation of concerns** — function logic remains untouched.

## Example Code

```python
import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] Function '{func.__name__}' took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(1.5)
    print("Finished slow function.")

@time_it
def add_numbers(a, b):
    time.sleep(0.5)
    return a + b
````

## Example Output

```
Finished slow function.
[TIMER] Function 'slow_function' took 1.5005 seconds.
[TIMER] Function 'add_numbers' took 0.5002 seconds.
Sum: 12
```

## How It Works

1. The `@time_it` syntax is shorthand for:

   ```python
   slow_function = time_it(slow_function)
   ```
2. The `wrapper` function inside `time_it`:

   * Runs code **before** the original function (`start_time`).
   * Calls the original function (`result = func(*args, **kwargs)`).
   * Runs code **after** it (`end_time` and print elapsed time).
3. `functools.wraps` ensures the wrapped function keeps its original name and docstring.

