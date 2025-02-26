def decorator(func):
    def wrapper():
        print("Starting function")
        func()
        print("Completing function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()