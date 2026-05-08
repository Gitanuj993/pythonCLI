#	finding root of a given polynomial equation using bisection method upto n stages.

# creating a linked list in python .
class Node :
	def __init__(self,coef = 1 ,  pow = 0 , next = None) :
		self.coef = coef
		self.pow = pow
		self.next = next
		

if __name__ == '__main__' :
	no_terms = int(input(" Enter total number of  terms in equations  : "))

	head = Node()
	temp = head
	for i in range(1,no_terms +1) :
		print("\n")
		print(" For term ", i )
		coef = int(input("Enter cofficient of term :  "  ))
		pow = int(input("Enter power of term :  " ))
		temp.next = Node(coef,pow)
		temp = temp.next
		
	# printing polynomial equation.
	temp = head.next
	while ( temp !=  None ) :
		print("( " , temp.coef,"X^",temp.pow," )"," + ", end = "" )
		temp = temp.next
	print("0")
	
	
	# finding range of root 
	x1 = None # negative number
	x2 = None # positive number
	test = 0
	while ( (x1 == None) or ( x2 == None) ) :
		total = 0	
		temp = head.next
		while ( temp != None) :
			#	solution of f(x)
			total += temp.coef * (test**temp.pow)				
			temp = temp.next		
		# checking condtion
		if total < 0 :
			x1 = test
		elif total > 0 :
			x2 = test
		else :
			print("root of the equation is : ",test)
		# increasing value of test if not found
		test += 1	
			
			
	# lets print the value of x1 and x2 , range ()
	print("x1 : " , x1 )
	print("x2 : " , x2 )			
                                                                       
	
	
	
		
		
