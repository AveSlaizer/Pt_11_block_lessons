def null_decorator(func):
    return func


def split_decorator(symbol):
    def main_decorator(func):
        def wrapper(*args, **kwargs):
            original_result = func(*args, **kwargs)
            modified_result = original_result.split(symbol)
            return modified_result

        return wrapper

    return main_decorator


def upper_decorator(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@split_decorator(symbol="O")
@upper_decorator
def main(n: int):
    return "Hello from main"[:n]


"""a = null_decorator(main)
print(a())"""
n = 10
print(main(n))
