

print("Hello World")
print(2+1)

st = 'Print only the words that start with s in this sentence'

string_list = st.split()

for word in string_list:
	if word.startswith('s'):
		print(word)


##		
for num in range(0, 11):
	if num%2==0:
		print(num)
		

##		
num_list = [num for num in range(1, 51) if num%3==0]
print(num_list)


##
st2 = 'Print every word in this sentence that has an even number of letters'

string_list2 = st2.split()

for word in string_list2:
	if len(word)%2==0:
		print(word)

		
##
for num in range(1, 100):
	if num%3==0:
		if num%5==0:
			print('FizzBuzz')
		else:
			print('Fizz')
	elif num%5==0:
		print('Buzz')
	else:
		print(num)
		
		
##
st3 = 'Create a list of first letters of every word in this string'

letter_list = [word[0] for word in st3.split()]

print(letter_list)