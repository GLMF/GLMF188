#!/usr/bin/python3

class Roman:
    units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    decades = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    dicos = [units, decades, hundreds]


    def __init__(self, decimal_number):
        self.__decimal = decimal_number
        self.__roman = self.__convert()


    def __getDecimal(self):
        return self.__decimal
    decimal = property(__getDecimal)


    def __getRoman(self):
        return self.__roman
    roman = property(__getRoman)


    def __partition(self):
        def calc_partition(n):
            while len(n) > 3:
                n = n[:-3]
            return int(n)

        strDecimal = str(self.__decimal)

        return list(map(calc_partition,
            [strDecimal[i:] for i in range(-3, -len(strDecimal)-3, -3)]))


    def __translateGroup(self, group, rank):
        if rank == 1 and group <=4 and group >= 1:
            return (group * 'M', 0)

        group = str('{:03d}'.format(group))

        symbol = ''
        for i in range(3):
                symbol += Roman.dicos[2-i][int(group[i])]

        return (symbol, rank)


    def __convert(self):
        result = ''

        for i, p  in enumerate(self.__partition()):
            conv = self.__translateGroup(p, i)
            if conv[1] == 0:
                result = conv[0] + result
            elif conv[0] != '':
                result = '(' + conv[0] + ')(' + str(conv[1]) + ')' + result

        return result


    def __str__(self):
        return self.__roman


if __name__ == '__main__':
    d = Roman(14000022)
    print('{} => {}'.format(d.decimal, d.roman))
