from typing import Union


def greeting(user="Unbekannt"):
    print(f"HALLO {user}")


# type hints: https://docs.python.org/3/library/typing.html (ab Python 3.5)

def addition(a: Union[int, float, str], b: Union[str, int, float]=None) -> Union[str, float, int]:
    """ Diese Funktion addiert Objekte

    :param a: usdrgb
    :param b: grdsrg
    :return: dkrtg
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a + b
    elif isinstance(a, str) and isinstance(b, str):
        result = a + "---" + b
    else:
        result = "etwas anderes..."
    return result
