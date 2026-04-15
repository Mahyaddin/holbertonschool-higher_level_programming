#!/usr/bin/python3
def safe_print_division(a, b):
    """İki tam ədədi bölür və nəticəni 'finally' blokunda çap edir."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
