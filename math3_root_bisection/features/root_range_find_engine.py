import time
class Node :
	def __init__(self,coef=1,pow=0,next = None) :
		self.coef = coef 
		self.pow = pow
		self.next = next
		
head = Node()
temp = head
temp.next = Node(2,1)
temp.next.next = Node(-1)
# printing linked list
temp = head.next
while ( temp !=  None ) :
	print("( " , temp.coef,"X^",temp.pow," )"," + ", end = "" )
	temp = temp.next
print("0")

# now performing operations 
#time.sleep(2)

# not used test_case = 10 # generally 0,1,2,3,4, .... # generator will be used

# 0 is not taken as value or range can be zero
x1 = None  # Negative
x2 = None  # positive
test = 0
while ( (x1 == None) or ( x2 == None) ) :
	total = 0	
	temp = head.next
	while ( temp != None) :
		#	solution of f(x)
		total += temp.coef * (test**temp.pow)		
		#
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

		
		
"""
Algorithm to find the range of root.

info : 
1. first we convert or shift  the valid equation  in left hand side inshort LHS 
2. putting LHS = 0 , which is our function equations say f(x)

1.Set x1 and x2 equal to None
2. we put x = 0,1,2,3 ... in function f(x)
3. evalute or solve the equation and get the answer.
4. if the answer is negative then x become range1 say x1
5. if the answer is positive then range2 or x2 is  x
6. if answer becomes 0 then  , x itself is root of the equations.
7. repeat and continue the process 2 to 6 until x1 or  x2  not have some value.



"""
