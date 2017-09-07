x=0
def fact(x):
	if x==1:
		return 1
	return x*fact(x-1)

n=int(input('n='))

print(fact(x))
