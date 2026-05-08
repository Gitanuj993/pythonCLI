#	finding root of a given polynomial equation using bisection method upto n stages.

# creating a linked list in python .
class Node :
	def __init__(self,coef = 1 ,  pow = 0 , next = None) :
		self.coef = coef
		self.pow = pow
		self.next = next
		

if __name__ == '__main__' :
	while True :
		try :
			no_terms = int(input(" Enter total number of  terms in equations  : "))
		except Exception as e  :
			print(e, " Try again !")
		else :
			break
	
	# creating of an equation
	head = Node()
	temp = head
	for i in range(1,no_terms +1) :
		print("\n")
		print(" For term ", i )
		while True :
			try :
				coef = int(input("Enter cofficient of term :  "  ))
				pow = int(input("Enter power of term :  " ))
			except Exception as e :
				print(e,"Try again !")
			else :
				break
		temp.next = Node(coef,pow)
		temp = temp.next
		
	# printing polynomial equation.
	temp = head.next
	print(" f(x) = ",end="")
	while ( temp !=  None ) :
		print("( " , temp.coef,"X^",temp.pow," )"," + ", end = "" )
		temp = temp.next
	print("0") # for empy thing
	print("\n")
	
	# finding range of root 
	x1 = None # negative number
	x2 = None # positive number
	x = 0 # for tring values
	while ( (x1 == None) or ( x2 == None) ) :
		total = 0	
		temp = head.next
		while ( temp != None) :
			#	solution of f(x)
			total += temp.coef * (x**temp.pow)				
			temp = temp.next		
		# checking condtion
		if total < 0 :
			x1 = x
		elif total > 0 :
			x2 = x
		else :
			print("root of the equation is : ",x)
			break
		# increasing value of test if not found
		x += 1	
			
			
	# lets print the value of x1 and x2 , range ()
	print("x1 : " , x1 )
	print("x2 : " , x2 )			                                                                       
	print("Root of the equation f(x) lie between ",x1," and ",x2)
	root_list = []
	stages = 5
	step = 0
	while  step < stages :
		x = ( x1 + x2 ) /2
		root_list.append(x)
		total = 0
		temp = head.next
		while ( temp != None) :
			total += temp.coef * (x ** temp.pow)
			temp = temp.next
		# conditions to change to value of x1 and x2 
		if total < 0 :
			x1 = x
		elif total > 0 :
			x2 = x
		else :
			print("Exact root of the equation is : ",x)
			break
		# to end 
		step +=1
		print("Root of the equation f(x) lie between ",x1," and ",x2)
			
	print(" approximate values of roots are : " , root_list)		
