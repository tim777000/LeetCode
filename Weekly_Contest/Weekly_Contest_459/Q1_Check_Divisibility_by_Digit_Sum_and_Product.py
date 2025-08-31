class Solution:
    def checkDivisibility(self, n: int) -> bool:
    	d_sum = 0
    	d_product = 1
    	i = n
    	while i > 0:
    		d_sum += i % 10
    		d_product *= i % 10
    		i = i // 10
    	return (n % (d_sum + d_product)) == 0
