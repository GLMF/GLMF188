#!/usr/bin/python3

class Dec:
    symbols = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

    def __init__(self, roman_number):
        self.__roman = roman_number
        self.__decimal = self.__convert()

    def __getDecimal(self):
        return self.__decimal
    decimal = property(__getDecimal)

    def __getRoman(self):
        return self.__roman
    roman = property(__getRoman)

    def __explode(self):
        result = []
        save = None

        for elt in self.__roman.split(')'):
            if elt.startswith('('):
                if save is None:
                    save = elt[1:]
                else:
                    for symbol in save:
                        result.insert(0, (symbol, int(elt[1:])))
                    save = None
            else:
                for symbol in elt:
                    result.insert(0, (symbol, 0))
        return result

    def __convert(self):
        value = 0
        pred = (None, None)
        partition = self.__explode()

        for elt in partition:
            if pred[0] is None and pred[1] is None:
                value = Dec.symbols[elt[0]] * 1000 ** elt[1]
            else:
                if Dec.symbols[elt[0]] < Dec.symbols[pred[0]] and elt[1] == pred[1]:
                    value -= Dec.symbols[elt[0]] * 1000 ** elt[1]
                else:
                    value += Dec.symbols[elt[0]] * 1000 ** elt[1]
            pred = elt
        return int(value)

    def __str__(self):
        return self.__roman

if __name__ == '__main__':
    d = Dec('(XIV)(2)(LII)(1)XLII')
    print('{} => {}'.format(d.roman, d.decimal))
