i = int(input('Enter a number to generate a Fibonacci sequence:-'))
num = 1
prev2 = 0 
prev1 = num
#i = 5
result = num

while i > 0:
	i = i - 1
	result = prev1 + prev2
	print (result, '=', prev1, '+', prev2)
	#print(result)
	prev2 = prev1
	prev1 = result
print('Done!')