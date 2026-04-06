#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Arqumentlərin sayını alırıq (skriptin adını çıxmaqla)
    count = len(sys.argv) - 1

    # İlk sətir: Say və doğru söz (argument/arguments) + sonluq (: / .)
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    # Arqumentlərin siyahısı
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
