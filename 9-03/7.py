
def hello():
    print('Hello, class!')

hello()


def some_function(name, job):
    print(name, 'is a', job)

some_function("Fiona", "developer")

#NON DEFAUL ARGUMENTS SHOULD BE FOLLOWED BY DEFAULT!
def some_function2(name, job = "developer"):
    print(name, 'is a', job)

some_function2("Fiona")

some_function2("Fiona", "manager")