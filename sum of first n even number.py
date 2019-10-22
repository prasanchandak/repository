# Python implementation to find sum of 
# first n even numbers 
	
# function to find sum of 
# first n even numbers 
def evensum(n): 
	curr = 2
	sum = 0
	i = 1
	
	# sum of first n even numbers 
	while i <= n: 
		sum += curr 
		
		# next even number 
		curr += 2
		i = i + 1
	return sum

# Driver Code 
n = 10
print("sum of first ", n, "even number is: ", 
	evensum(n)) 
