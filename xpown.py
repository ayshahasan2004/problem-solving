class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        def power(exponent: int) -> float:
            if exponent == 0:
                return 1.0

            half_power = power(exponent // 2)
            result = half_power * half_power
            if exponent % 2 == 1:
                result *= x
            return result

        return power(n)