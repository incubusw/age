driving = input('Have you ever drived car?')
if driving != 'Yes'and driving != 'No':
	print('Answer can only be Yes or No')
	raise SystemExit
age = input('How old are you?')
age = int(age)
if driving == 'Yes':
	if age >= 18:
		print('You pass the exam!!')
	else:
		print('You are too young to drive car!!')
elif driving == 'No': 
	if age >= 18:
		print('Please prepare to take the exam.')
	else:
		print('Just wait for a couple of years.')

















