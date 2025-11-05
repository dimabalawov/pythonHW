import math
from numbers import Real
from typing import Union

class Fraction:
    def __init__(self, n: int, d: int):
        if not isinstance(n, int) or not isinstance(d, int):
            raise TypeError("N і D мають бути int.")
        if d == 0:
            raise ValueError("D не може бути 0.")

        if d < 0:
            n = -n
            d = -d
            
        self.n = n
        self.d = d
        self.reduce()

    def __str__(self) -> str:
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def __repr__(self) -> str:
        return f"Fraction({self.n}, {self.d})"

    def reduce(self) -> None:
        divisor = math.gcd(self.n, self.d)
        self.n //= divisor
        self.d //= divisor

    def to_float(self) -> float:
        return self.n / self.d

    def __float__(self) -> float:
        return self.to_float()
    
    @staticmethod
    def from_float(val: float, prec: int = 1000) -> 'Fraction':
        if not isinstance(val, Real):
            raise TypeError("Тільки числа (float/int) сюди.")
            
        if val == 0:
            return Fraction(0, 1)
            
        num = val
        den = 1
        
        while abs(num - round(num)) > 1e-9 and den < prec:
            num *= 10
            den *= 10
            
        return Fraction(int(round(num)), den)

    def _get_fraction(self, other: Union['Fraction', int, float]) -> 'Fraction':
        if isinstance(other, Fraction):
            return other
        if isinstance(other, int):
            return Fraction(other, 1)
        if isinstance(other, (float, Real)):
            return Fraction.from_float(other)
        raise TypeError("Ліл, не той тип.")

    def __add__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        o_f = self._get_fraction(other)
        new_n = self.n * o_f.d + o_f.n * self.d
        new_d = self.d * o_f.d
        return Fraction(new_n, new_d)

    def __radd__(self, other: Union[int, float]) -> 'Fraction':
        return self.__add__(other)
    
    def __sub__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        o_f = self._get_fraction(other)
        new_n = self.n * o_f.d - o_f.n * self.d
        new_d = self.d * o_f.d
        return Fraction(new_n, new_d)

    def __rsub__(self, other: Union[int, float]) -> 'Fraction':
        return Fraction(other, 1) - self

    def __mul__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        o_f = self._get_fraction(other)
        new_n = self.n * o_f.n
        new_d = self.d * o_f.d
        return Fraction(new_n, new_d)

    def __rmul__(self, other: Union[int, float]) -> 'Fraction':
        return self.__mul__(other)

    def __truediv__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        o_f = self._get_fraction(other)
        
        if o_f.n == 0:
            raise ZeroDivisionError("На нуль не ділимо.")
            
        new_n = self.n * o_f.d
        new_d = self.d * o_f.n
        return Fraction(new_n, new_d)
    
    def __rtruediv__(self, other: Union[int, float]) -> 'Fraction':
        return Fraction(other, 1) / self

if __name__ == "__main__":
    
    print("Тести")
    f1 = Fraction(9, -12)
    f2 = Fraction(1, 4)
    f_float = Fraction.from_float(0.125)

    print(f"1. f1 (9/-12) -> {f1}")  # -3/4
    print(f"2. 0.125 -> {f_float}") # 1/8
    print(f"3. f1 як float: {float(f1)}")

    print(f"\nОперації")
    print(f"{f1} + {f2} = {f1 + f2}")   # -3/4 + 1/4 = -2/4 = -1/2
    print(f"1 - {f1} = {1 - f1}")       # 1 - (-3/4) = 7/4
    print(f"{f2} * 8 = {f2 * 8}")       # 1/4 * 8 = 2/1
    print(f"1 / {f_float} = {1 / f_float}") # 1 / 1/8 = 8/1