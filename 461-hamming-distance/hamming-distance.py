class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = 0
        xor = x ^ y
        conversion = bin(xor)[2:]

        digits_list = [int(digit) for digit in str(conversion)]
        for i in digits_list:
            if i == 1:
                c+=1
        return c

        