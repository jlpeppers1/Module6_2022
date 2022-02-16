#Docstring


#Example, delete this
def a_function():
    #inner function
    def an_inner_function():
        #inner funciton code; double indented
        print("This must be called to be executed")
    #singe indented, inner function code call
    an_inner_function()

def measurements(a_list):
    def area(a_list):
        pass
    def perimeter(a_list):
        pass
    pass
    #Fill in area and perimeter inner function calculations
    #assign a variable to the output of the area function call
    #assign a variable to the output of the perimeter function call
    #construct a string like "Perimeter = 11.0 Area = 7.14" based on the outputs
    #return that string #because it is printed in the driver code


#Driver
if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)
