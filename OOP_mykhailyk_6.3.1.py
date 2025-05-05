from OOP_mykhailyk_531 import Rational

class RationalList:
    def __init__(self, elements=None):
        self._list = []
        if elements:
            for el in elements:
                self._add_element(el)

    def _add_element(self, el):
        if isinstance(el, Rational):
            self._list.append(el)
        elif isinstance(el, int):
            self._list.append(Rational(el))
        else:
            raise TypeError("Elements must be Rational or int")

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self._list[index] = value
        elif isinstance(value, int):
            self._list[index] = Rational(value)
        else:
            raise TypeError("Value must be Rational or int")

    def __len__(self):
        return len(self._list)

    def __add__(self, other):
        result = RationalList(self._list)
        if isinstance(other, RationalList):
            result._list.extend(other._list)
        elif isinstance(other, Rational):
            result._add_element(other)
        elif isinstance(other, int):
            result._add_element(other)
        else:
            raise TypeError("Can only add RationalList, Rational, or int")
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for el in other._list:
                self._add_element(el)
        elif isinstance(other, Rational):
            self._add_element(other)
        elif isinstance(other, int):
            self._add_element(other)
        else:
            raise TypeError("Can only add RationalList, Rational, or int")
        return self

    def sum(self):
        total = Rational(0)
        for el in self._list:
            total += el
        return total

    def __iter__(self):
        sorted_list = sorted(
            self._list,
            key=lambda r: (-r.denominator, -r.numerator)
        )
        return iter(sorted_list)

def read_rational_list_from_file(filename):
    rl = RationalList()
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            for token in tokens:
                if '/' in token:
                    n, d = map(int, token.split('/'))
                    rl += Rational(n, d)
                else:
                    rl += int(token)
    return rl


for fname in ['input01.txt', 'input02.txt', 'input03.txt']:
    rl = read_rational_list_from_file(fname)
    print(f"Сума чисел у файлі {fname}: {rl.sum()}")