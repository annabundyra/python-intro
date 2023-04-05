#args, kwargs????

def print_arguments(*args):
    print(*args)

print_arguments(1, 2, 3, 4, 5, 6 ,7)

def print_kwarguments(**kwargs):
    print(*kwargs)

print_kwarguments(name = "Fiona", age = "25", job = "developer")

def print_ak(*args, **kwargs):
    print("args",args)
    print("kwargs", kwargs)

print_ak(1, 2, 3, name = "Fiona", age = "25", job = "developer")