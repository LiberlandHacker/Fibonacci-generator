num = int(input())


sequence = [0, 1, 1]
num -= 3

def fibonacci(n):
	#complete the recursive function
	
	n1 = sequence[-2]
	n2 = sequence[-1]
	sequence.append(n1+n2)

	n -= 1
	if n > 0:
		fibonacci(n)





fibonacci(num)

for number in sequence:
		print(number)


