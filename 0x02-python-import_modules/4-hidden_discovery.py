#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    print('\n'.join([d for d in dir(hidden_4) if d[:2] != '__']))
