i = int(input('Enter a number to generate a Fibonacci sequence:-'))
N = i
num = 1
prev2 = 0 
prev1 = num
result = num
while i > 0:
	i = i - 1
	result = prev1 + prev2
	print (result, '=', prev1, '+', prev2) #you can use this print line or the below one
	#print(result)
	prev2 = prev1
	prev1 = result
print('Here is the Fibonacci sequence up to ', N, ' !')
