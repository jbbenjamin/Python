def lesser_of_two_evens(num1, num2):
if num1 % 2 == 0 and num2 % 2 == 0:
	if num1 < num2:
		return num1
	else:
		return num2
else:
	if num1 > num2:
		return num1
	else:
		return num2
		
##

def same_letter(two_word_string):
two_word_string = two_word_string.lower()
string_list = two_word_string.split()
if string_list[0][0] == string_list[1][0]:
	return True
else:
	return False
	
##

def other_side_of_seven(num):
	return 7 - (2(num - 7))
	
##

def old_macdonald(name):
	name = name.lower()
	name = name.capitalize()
	name[3].upper
	first_half = name[:3]
	second_half = name[3:]
	result = first_half.capitalize() + second_half.capitalize()
	return name
	
##

def master_yoda(phrase):
	yoda_phrase = ''
	phrase_list = phrase.split(' ')
	while phrase_list.numOfItems() > 0:
		yoda_phrase += phrase.pop()
	return yoda_phrase
	
##

def almost_there(n):
	if abs(100 - n) <= 10 or abs(200 - n) <= 10:
		return True
	else:
		return False
		
##
		
def laughter(pattern,text):
	length = text.len()
	i = 0
	numOfOccurrences = 0
	while i < length:
		if text.find(pattern) == True:
			numOfOccurrences += 1
	i += 1

##

def paper_doll(word):
	triple_word = ''
	for letter in word:
		triple_word = triple_word + letter + letter + letter
	return triple_word

##	

def blackjack(a,b,c):
	sum = a + b + c
	if sum <= 21:
		print(sum)
	elif sum > 21 and (a == 11 or b == 11 or c == 11):
		sum -= 10
		if sum > 21:
			print('BUST')
		else:
			print(sum)
	else:
		print('BUST')
return
		
def summer_69(arr):
	six_thru_nine = False
	sum = 0
	for num in arr:
		if num == 6:
			six_thru_nine = True
		elif num == 9:
			six_thru_nine = False
		else:
			if six_thru_nine == True:
				sum += 0
			else:
				sum += num
	return sum
	

	