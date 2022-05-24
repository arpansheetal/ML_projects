class ABC:
    def __init__(self) -> None:
        self.test_var = None

if __name__ == '__main__':
    v = ABC()
    print(v.test_var == None)