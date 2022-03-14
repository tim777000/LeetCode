class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        org_abs_dividend = abs(dividend)
        org_abs_divisor = abs(divisor)
        quotient = 0
        temp_dividend = org_abs_dividend
        temp_divisor = org_abs_divisor
        while (temp_dividend >= org_abs_divisor):
            temp_divisor = org_abs_divisor
            shift_counter = 0
            while (temp_dividend >= temp_divisor):
                temp_divisor <<= 1
                shift_counter += 1
            temp_dividend -= (org_abs_divisor << (shift_counter-1))
            quotient += (1 << (shift_counter-1))

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return -2147483648 if ((quotient*(-1)) < -2147483648) else quotient*(-1)

        return 2147483647 if (quotient > (2147483647-1)) else quotient