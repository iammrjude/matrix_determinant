# Function to calculate a 2*2 Matrix
def mat_2_2():
	print("FOR A 2*2 MATRIX ; ")
	print()
	if row==2 and column==2:
		R1C1=int(input("Enter the number contained in column 1 of row 1: "))
		R1C2=int(input("Enter the number contained in column 2 of row 1: "))
		R2C1=int(input("Enter the number contained in column 1 of row 2: "))
		R2C2=int(input("Enter the number contained in column 2 of row 2: "))
		Det=str(((R1C1*R2C2)-(R1C2*R2C1)))
		print()
		print("The Determinant is: "+Det)

# Function to calculate a 3*3 matrix
def mat_3_3():
	print()
	print("FOR a 3*3 Matrix ; ")
	print()
	if row==3 and column==3:
		R1C1=int(input("Enter the number contained in column 1 of row 1: "))
		R1C2=int(input("Enter the number contained in column 2 of row 1: "))
		R1C3=int(input("Enter the number contained in column 3 of row 1: "))
		R2C1=int(input("Enter the number contained in column 1 of row 2: "))
		R2C2=int(input("Enter the number contained in column 2 of row 2: "))
		R2C3=int(input("Enter the number contained in column 3 of row 2: "))
		R3C1=int(input("Enter the number contained in column 1 of row 3: "))
		R3C2=int(input("Enter the number contained in column 2 of row 3: "))
		R3C3=int(input("Enter the number contained in column 3 of row 3: "))
		a=int((R2C2*R3C3)-(R2C3*R3C2))
		b=int((R2C1*R3C3)-(R2C3*R3C1))
		c=int((R2C1*R3C2)-(R2C2*R3C1))
		d=int(R1C1*a)
		e=int(R1C2*b)
		f=int(R1C3*c)
		print()
		Det1=str((d-e+f))
		print("The Determinant is: "+Det1)

# Function to start the program		
def start():
	global row
	global column
	print("This Program will calculate the Determinant of a 2*2 matrix or a 3*3 matrix")
	print()
	row=int(input("How many rows? : "))
	print()
	column=int(input("How many columns? : "))
	print()
	
# Function that Decides which matrix to calculate		
def condition():
	if row==2 and column==2:
		mat_2_2()
	elif row==3 and column==3:
		mat_3_3()
	else:
		print("This program can only calculate the determinant for a 2*2 matrix or a 3*3 matrix" )
		print("")
		start()
		
# Another Function to start the program	
def start1():
	global row
	global column
	print("This Program will calculate the Determinant of a 2*2 matrix or a 3*3 matrix")
	print()
	row=int(input("How many rows? : "))
	print()
	column=int(input("How many columns? : "))
	print()
	# Condition is called this is what makes the program to calculate the determinant
	condition()
	
# CONDITION 1
def condition1():
	if row==2 and column==2:
		mat_2_2()
	elif row==3 and column==3:
		mat_3_3()
	else:
		print("This program can only calculate the determinant for a 2*2 matrix or a 3*3 matrix" )
		print("")
		start()
		condition()

# CONDITION 2		
def condition2():
	if row==2 and column==2:
		mat_2_2()
	elif row==3 and column==3:
		mat_3_3()
	else:
		print("This program can only calculate the determinant for a 2*2 matrix or a 3*3 matrix" )
		print("")
		start()
		#If user enters a invalid matrix e.g '2*1' , Condition1 is called to start the program again
		condition1()

#Program has started Running	
start()
								
#Condition2() has been called
condition2()		

#Loop to Restart the Program		
print()	
print("Do you want to run the program again? ")

def response():
	print()
	response=input("YES/NO: ")
	print()
	if response=="YES":
		start1()
	elif response=="NO":
		print("[Program finished]")
	else:
		print("Invalid answer. Type either 'YES' or 'NO' ")
		response2=input("YES/NO: ")
		print()
		if response2=="YES":
			start1()
		elif response2=="NO":
			print("[Program finished]")
	
#response() Function is called
response()
# In summary when the Function 'start()' is called the program starts running
#    Then the Function 'condition2()' is called.
#    If the user enters a wrong matrix, 'condition1()' is called. And if the user again enters a wrong matrix  'condition()' is called.
#    If the user finally enters a correct marix, the program successfully calculates the determinant of the r*n matrix.
#    Then a loop starts that asks if you want to restart the program. If the user enters 'YES' the program is restarted.		