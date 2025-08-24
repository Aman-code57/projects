def adds(func):
    def wrapper(*args , **kwargs):
        print("before execution")
        result = func(*args ,**kwargs)
        print("after execution")
        return result
    return wrapper


@adds
def add(a,b):
    return a + b
print(add(5,3))