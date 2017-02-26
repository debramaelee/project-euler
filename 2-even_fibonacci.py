# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

# METHOD 1

fib_nums = [1, 1]
i = 0
j = 0
current = fib_nums[i]
sum = 0

while current < 20:

	if current % 2 == 0:
		sum = sum + current
		print sum
	current = fib_nums[i] + fib_nums[j]
	if current < limit:
		fib_nums.append(current)
	i += 1
	j += 1

print sum

# METHOD 2

current = 1
previous = 1

while current < 20:
	if current % 2 == 0:
		sum += current

	current, previous = current + previous, current
	# manual swap version
	# temp = current
	# current = current + previous
	# previous = temp

print sum

# METHOD 3

def fib(n):
	if n == 1 or n == 2:
		return 1
	return fib(n-1) + fib (n-2)

for i in range(1, 10):
	print fib(i)
