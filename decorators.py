from collections import deque
from datetime import datetime


# Task 1 Write a decorator that ensures a function is only called by users with a specific role.

def is_admin(func):
    def wrapper(**kwargs):
        match kwargs["user_type"]:  # if user_types will be more, we can add more variants of reactions
            case "admin":
                func("admin")
                return True  # return for testing by assert
            case _:
                print("Permission denied")  # it also could be done by throw Exception

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print(f"You are {user_type}! You can do anything!")


assert show_customer_receipt(user_type='user') is None
assert show_customer_receipt(user_type='admin') is True


# Task 2 Write a decorator consist of try-except block

def try_except_decorator(func):
    def wrapper(*args):
        try:
            return func(args[0], args[1])
        except Exception as e:
            print(f"Some errors appeared: {e.args[0]}")
    return wrapper


@try_except_decorator
def divided_function(a: str, b: str):
    return int(a) / int(b)


assert divided_function(4, 2) == 2
assert divided_function(4, 0) is None


# Task 3 Optional: Decorator that will check types

def check_types(func):
    def wrapper(*args):
        try:
            start_arg_code = 97
            for arg in args:
                if not isinstance(arg, int):
                    raise TypeError(f"Argument {chr(start_arg_code)} must be int, not {type(arg).__name__}")
                start_arg_code += 1
            return func(args[0], args[1])
        except Exception as e:
            print(e)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


assert add(1, "2") is None
assert add(2, 3) == 5
assert add(2.5, 3) is None


# This decorator has been already done on the last lecture
# Task 4 Create a function that caches the result of a function.
def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)  # unique key for detecting if func with such params hac been already called
        if key not in cache:
            cache[key] = func(*args, **kwargs)  # add to dictionary new value is not exist such key
        return cache[key]

    return wrapper


# Task 5 Write a decorator that adds a rate-limiter to a function
def limiter(func):
    max_call_per_minute = 5
    call_history = deque(maxlen=max_call_per_minute)

    def wrapper(*args, **kwargs):
        now = datetime.now()
        if len(call_history) < max_call_per_minute:
            # if there is free place in the call history, add the current time
            call_history.append(now)
        else:
            # if the call history is full, check if the oldest timestamp is more than 1 minute ago
            oldest_call = call_history[0]
            elapsed_time = (now - oldest_call).total_seconds()
            if elapsed_time < 60:
                # if not enough time has elapsed, raise an exception
                raise Exception(
                    f"Rate limit exceeded. Can only call {func.__name__} {max_call_per_minute} times per minute.")
            else:
                # if enough time has elapsed, remove the oldest timestamp and add the current time
                call_history.popleft()
                call_history.append(now)

        func(*args, **kwargs)

    return wrapper
