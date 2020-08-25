def function1():
	print("I am a function")

def function2(arg1, arg2):
	print(arg1, " ", arg2)

def cube(x):
	return x*x*x

def power(num, x=1):
	result=1
	for i in range(x):
		result = result * num
	return result

def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result

# function1()
# print("-----")
# print(function1())
# print("-----")
# print(function1)

# function2(10, 20)
# print("-----")
# print(function2(10, 20))
# print("-----")
# print(cube(4))
# print("-----")
# print(power(2))
# print("-----")
# print(power(2,3))
# print("-----")
# print(power(x=3, num=2))
# print("-----")
print(multi_add(3, 4, 5, 10, 4, 8))
