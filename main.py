class SimpleCalculator:
	def __init__(self):
		self.history=[]
	def evaluate_expression(self, input_expression):
		s=input_expression
		s=" "+s+" "
		l=[]
		c=''
		for i in range (0,len(s)):
			if s[i]==" ":
				if c!="":
					l.append(c)
				c=""
			else:
				if ((s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/")) :
					if c!="":
						l.append(c)
					l.append(s[i])
					c=""
				else:
					c=c+s[i]
		if len(l)==4:
			if l[0]=="-":
				l.remove("-")
				l[0]="-"+l[0]
		if len(l) != 3:
			self.history.append("Error")
			return "Error"

		else:
			if l[1] == "+":
				self.history.append(float(l[0]) + float(l[2]))
				return (int(l[0]) + int(l[2]))
			if l[1] == "-":
				self.history.append(int(l[0]) - int(l[2]))
				return (int(l[0]) - int(l[2]))
			if l[1] == "*":
				self.history.append(int(l[0]) * int(l[2]))
				return (int(l[0]) * int(l[2]))
			if l[1] == "/":
				if l[2]!=0:
					self.history.append(int(l[2]) / int(l[0]))
					return (int(l[2]) / int(l[0]))
				else:
					print("Error")
					return ValueError("Error")
	def get_history(self):
		return(self.history)

class Stack:
	def __init__(self):
		self.items=[]

	def push(self, item):
		self.items.append(item)


	def peek(self):
		return(self.items[-1])

	def pop(self):
		self.items.pop()

	def is_empty(self):
		if self.items==[]:
			return True
		return False

	def __str__(self):
		c=""
		for i in range (len(self.items)-1,-1,-1):
			c=c+str(self.items[i])+" "
		return(c)

	def __len__(self):
		return(len(self.items))

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		SimpleCalculator.__init__(self)

	def tokenize(self, input_expression):
		c=[]
		for i in input_expression:
			if i!=" ":
				c.append(i)
		return(c)

	def check_brackets(self, list_tokens):
		A=Stack()
		for i in list_tokens:
			if i=="{" or i=="(":
				if not A.is_empty():
					if A.peek()=="(" and i=="{":
						return False
				A.push(i)
			elif i=="}" or i==")":
				if A.is_empty():
					return False
				else:
					if (i==")" and A.peek()=="{") or (i=="{" and A.peek()==")"):
						return False
					A.pop()
		return(A.is_empty())

	def evaluate_list_tokens(self, list_tokens):
		A=Stack()
		B=Stack()
		for i in list_tokens:
			if i=="(" or i=="{":
				A.push(i)
			elif i=="+" or i=="-" or i=="*" or i=="/":

				A.push(i)
			elif i==")":
				c=""
				C=SimpleCalculator()
				while A.peek()!="(":
					c=c+str(B.peek())
					B.pop()
					c=c+str(A.peek())
					A.pop()
					c=c+str(B.peek())
					B.pop()
					B.push(C.evaluate_expression(c))
					c=""
				A.pop()
			elif i=="}":
				c=""
				C=SimpleCalculator()
				while A.peek()!="{":
					c=c+str(B.peek())
					B.pop()
					c=c+str(A.peek())
					A.pop()
					c=c+str(B.peek())
					B.pop()
					B.push(C.evaluate_expression(c))
				A.pop()
			else:
				B.push(i)
		self.history.append(str(B.peek()))
		return(str(B.peek()))

	def evaluate_expression(self, input_expression):
		print(self.tokenize("(((2+3)*3+2)/4)"))
		if self.check_brackets(self.tokenize(input_expression)):
			return(self.evaluate_list_tokens(input_expression))
		else:
			return("ERROR")



















