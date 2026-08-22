class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        temp = n
        while temp > 0:
            temp, digit = divmod(temp, 10)
            digit_sum += digit
            digit_product *= digit

        total_sum = digit_sum + digit_product
        return n % total_sum == 0
        