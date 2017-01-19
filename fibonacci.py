i = int(input('Enter a number to generate a Fibonacci sequence:-'))
N = i

prev2 = 1 
prev1 = 0

result = prev1
if i <=0:
	print('Enter positive integer')
elif i ==1:
	print('Here is the Fibonacci sequence up to', N, '!')
	print(prev1)
else: 
	print('Here is the Fibonacci sequence up to', N, '!')
	print(prev1)
	print(prev2)
	while i >= 3:
		i = i - 1
		result = prev1 + prev2
		#print(result, end=',')
		print(result)
		prev1 = prev2
		prev2 = result
