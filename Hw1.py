''' Assignment 1 : Mini guessing game '''

name=input("what is your name? \n")
print("Hello" + " " +name+ " " + "let us play a game")
print("Guess a random number between 1 to 100 and I will try to guess it")

low=0
high=100
mid=50
count=0

play="yes"
while (play=="yes"):

	choice=input("Is the number " +str(mid) + "? yes/no \n Ans.")
	count=count+1

	if(choice=="yes"):
			print("Yeyy! I got it in " +str(count)+ " tries! ")
	else:		
		choice2=input("Is the number greater than" +str(mid) + "yes/no? \n Ans.")

		while (choice=="no" and (choice2=="yes" or choice2=="no")):
				while (choice2 == "yes"):
					low=mid+1
					mid=int((high+low)//2)
					choice=input("Is the number " +str(mid)+ "? yes/no? \n Ans.")
					if(choice=="no"):
						count=count+1
						choice2=input("Is the number greather than " +str(mid)+ "? yes/no? \n Ans.")                                                
					elif(choice=="yes"):
						count=count+1
						print("\tI guessed it in " + str(count) + " tries.")
						break

				while (choice2=="no"):
					high=mid-1
					mid=int((high+low)//2)
					choice=input("Is the number " +str(mid)+ "? yes/no? \n Ans.")
					if(choice=="no"):
						count=count+1
						choice2=input("Is the number greather than " +str(mid)+ "? yes/no? \n Ans.")                                                
					elif(choice=="yes"):
						count=count+1
						choice2=("I guess it in " +str(count)+ "tries")
						break
play=input("Want to play again? yes/no \n")
						