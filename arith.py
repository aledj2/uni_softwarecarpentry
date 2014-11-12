import sys
num1=float(sys.argv[1])
math=sys.argv[2]
num2=float(sys.argv[3])

def arith(num1,math,num2):
	''' enter sum in form 'number one' <space> 'math function (+-/*^)' <space> 'number 2' ''' 
	if math == '+':
		x=num1 + num2
		print x
	elif math == '-':
		x=num1 - num2
		print x
	elif math == '*':
		x=num1 * num2
		print x
	elif math == '/':
		x=num1 / num2
		print x
	elif math == '^' or math =='^^':
		x=int(num1) ^ int(num2)
		print x ,"NB Numbers have been rounded down to nearest value)"
	else :
		x="error"
		print x

arith(num1,math,num2)
