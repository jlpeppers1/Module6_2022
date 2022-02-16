def a_decorator(func):
    def wrapper():
        print("Do something before the function call.")
        func()  # call the function!
        print("Do something after the function call.")
    return wrapper


def a_function():
    print("Hello, World!")


def b_function():
    print("Au revoir!")


if __name__ == '__main__':
    # send a_function to the decorator, save in say_hello function
    say_hello = a_decorator(a_function)
    say_hello()

    say_goodbye = a_decorator(b_function)
    say_goodbye()
