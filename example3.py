def gensquares(N):
	for x in range(N):
		yield x*x

for x in gensquares(10):
	print(x)
	
#______________________

print("\n\n")

#______________________	
import random

def rand_num(low, high, n):

	for x in range(n):
		yield random.randint(low, high)
	
for num in rand_num(5, 50, 7):
	print(num)
	
#______________________
s = 'hello'
i = iter(s)

#print(next(i))
#______________________