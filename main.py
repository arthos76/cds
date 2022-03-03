from src.modulA import greeting, addition


def run():
    greeting(user="Marco")
    print(addition(a=1, b=2))
    print(addition(a=1, b=2.5))
    print(addition("1", "2"))
    print(addition(a=2))


if __name__ == '__main__':
    # help(addition)
    run()
