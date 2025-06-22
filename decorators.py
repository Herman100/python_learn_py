def announce(f):
    def wrapper(*args, **kwargs):
        print("about to run function")
        name, rest = args
        f(name)
        print("done with the function")

    return wrapper


@announce
def hello(name="Doe"):
    print(f"Welcome to the team {name}")


hello("Janice", "Jermai")
