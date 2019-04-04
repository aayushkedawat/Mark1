class Calculator():
	def __init__(self,a,b):
        	self.a=a
        	self.b=b
	def add(self):
		return self.a+self.b
	def substract(self):
		return self.a-self.b
firstNumber = int(input("Enter first number"))
secondNumber = int(input("Enter Second Number"))
num = Calculator(firstNumber,secondNumber)
choice = int(input("Enter 1 for Addition\nEnter 2 for Substraction\n"))
if choice==1:
	print(num.add())
elif choice==2:
	print(num.substract())
else:
	print("Enter Valid Number")
