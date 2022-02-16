def a_function():
    def an_inner_function():
        print("This must be called to be executed!")
    an_inner_function()
    an_inner_function()

if __name__ == '__main__':
    a_function()
