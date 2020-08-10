
# Class Starts
class ArmstrongNumber:

	# Function to check a number is Armstrong or not
	def checkNumber(self,user):
		
		users = user
		sumation = 0
		check = True
		for i in range(len(str(user))):
			a = int(user%10)
			user = int(user/10)
			sumation += a ** 3
			
		if sumation == users:
			print("Yes, It's an ARMSTRONG number.")
		else: 
			print("Not an ARMSTRONG number.")



	# Function to find all the Armstrong number in a range.
	def findArmstrong(self, starts, ends):
		number = []

		for i in range(starts, ends+1):
			user = i
			sumation = 0
			for j in range(len(str(i))):
				a = int(i%10)
				i = int(i/10)
				sumation += a ** 3 

			if sumation == user:
				number.append(sumation)
		if number is not None:
			print("\nThese are ARMSTRONG number: {}\n".format(number))
		else:
			print("\nNo number found!!!\n")

# Class Ends




	# Main function starts
if __name__ == "__main__":
	try:
		exit = True
		while exit == True:	
			print('''
				\tArmstrong
				1. Check A Number
				2. Find Armstrong List
				3. Exit
				''')

			obj = ArmstrongNumber()			# Creating Object of the class.

			choose = int(input("Choose an option : "))
			if choose == 1:
				user = int(input("Number: "))
				obj.checkNumber(user)
			elif choose == 2:
				user = int(input("Starts From: "))
				user1 = int(input("Ends On: "))
				obj.findArmstrong(user, user1)
			elif choose == 3:
				print("Good Bye...")
				break
			else:
				print("Wrong Input.")

	#Error Handling		
	except KeyboardInterrupt:
		print("\n\nYou messedup with the procudure.\n")
	except ValueError:
		print("\n\nGiven wrong value. Try again.\n")
