#!/usr/bin/python3
if __name__ == "__main__":
    """Print names from a hidden module"""
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print("{}".format(name))
