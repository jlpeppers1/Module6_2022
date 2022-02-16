def hello(first_name, last_name, middle_initial=''):
    print(f'Hello {first_name} {middle_initial} {last_name}')

#Wont compile; has arguments after default arguments
#def hello(middle_initial='', first_name, last_name):
#    print(f'Hello {first_name} {middle_initial} {last_name}')

hello('Joe', "Smith", "John")
#not passing in a middle name, so it uses the default
hello('Joe', "Smith")


def any_function(argument1, argument2, default_argument='any default value'):
    pass

                    #string         #int        #float    #list (in this case list of str)
def person_data(first_name='joe', age=103, pay_rate=3.50, direct_reports=['john', 'jim']):
    print(f'Manager {first_name} is making ${pay_rate:.2f} at age {age}.')
    print("Their direct reports are:")
    for report in direct_reports:
        print(report)

person_data()
person_data("Jim")
person_data("Jim", 25)
person_data("Jim", 25,15.00,["Joe", "Josh", "James"])
