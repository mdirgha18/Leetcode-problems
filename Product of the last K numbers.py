class ProductOfNumbers:

    def __init__(self):
        # Initialize an empty list to store the prefix product of numbers
        self.list = []
        # Variable to keep track of the running product of numbers
        self.prod = 1
        

    def add(self, num: int) -> None:
        if num == 0:
            # If the number is 0, reset the list and the product tracker
            # Because any product involving 0 will be 0, so we start fresh
            self.list = []
            self.prod = 1
        else:
            # Update the cumulative product
            self.prod *= num
            self.list.append(self.prod)
        

    def getProduct(self, k: int) -> int:
        if len(self.list) < k:
            # If there are fewer than k elements, return 0 (because at some point a zero was encountered)
            return 0 
        if len(self.list) == k:
            # If exactly k elements exist, return the last stored product
            return self.list[-1]
        # Otherwise, divide the last  stored product by the product of elements before the last k 
        return self.list[-1] // self.list[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
