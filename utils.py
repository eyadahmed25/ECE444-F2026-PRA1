class utils:
    def reversed(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        return int(str(number)[::-1])

    def formatter(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        binary = bin(number)[2:]
        octal = oct(number)[2:]
        return binary, octal

