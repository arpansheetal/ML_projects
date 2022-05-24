class ABC:
    def __init__(self) -> None:
        self.test_var = None

    def check_None(self):
        # Check test var for None
        return self.test_var == None

if __name__ == '__main__':
    v = ABC()
    print(v.check_None())