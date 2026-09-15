class utils:
    def reversed(self, number):
        return int(str(number)[::-1])

    def formatter(self, number):
        binary = bin(number)[2:]
        octal = oct(number)[2:]
        return binary, octal

