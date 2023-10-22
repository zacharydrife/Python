# Magic_8-Ball.py 
# This will be a Portfolio Project where I am building a Python 3 "Magic 8-Ball" that can answer any "Yes" or "No" questions and offer a fortunes after asking the users for input.


print("I am the Magic 8-Ball! Bring to me your troubles child so that I may bless you with a fortune but beware, the answer may not be that which you seek.\n")
name = input("Tell me your name my child." + "\nMy name is: ")
question = input("\nah " + name + ", what is your question my child?\n")
answer = ""
import random
random_number = random.randint(1,9)

if random_number == 1:
  answer = ("Yes - definitely.")
elif random_number == 2:
  answer = ("It is decidedly so.")
elif random_number == 3:
  answer = ("Without a doubt.")
elif random_number == 4:
  answer = ("Reply hazy, try again.")
elif random_number == 5:
  answer = ("Ask again later.")
elif random_number == 6:
  answer = ("Better not tell you now.")
elif random_number == 7:
  answer = ("My sources say no.")
elif random_number == 8:
  answer = ("Outlook not so good.")
elif random_number == 9:
  answer = ("Very doubtful.")
else:
  answer = ("Error")

if question == "":
  print("Even in all of my wisdom, I cannot provide a fortune without you asking for one!")

else:
    print("\n" + name + " asks : " + question)
    print("Magic 8-Ball's answer: " + answer)
