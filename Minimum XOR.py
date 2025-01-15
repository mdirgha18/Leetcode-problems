class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Calculate the difference between the number of set bits (is in binary)
        # in num1 and num2. The goal is to make the number of set bits in num1
        # equal to that in num2 while keeping the result as small as possible
        diff_set_bits = num1.bit_count() - num2.bit_count()
        if diff_set_bits > 0:
            # If num1 has more set bits than num2:
            # Remove the excess set bits from num1 by resetting the least significant set bits
            # Reset the 'diff_set_bits' least significant bits of the number 'num1'
            for _ in range(diff_set_bits):
                num1 &= num1 - 1
        else:
            # Set the 'diff_set_bits' least insignificant bits of the number 'num1'
            # If num1 has fewer set bits than num2: 
            # Add the required number of set bits to num1 by setting the least significant unset bits
            for _ in range(-diff_set_bits):
                # Set the least significant unset bit in num1
                num1 |= num1 + 1

        # Return the modified num1, which now has the same number of set bits as num2
        return num1

        
