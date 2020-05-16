# Multiplication Tables
tup1 = (3, 4, 5, 6, 7, 8, 9)
tup2 = (3, 4, 5, 6, 7, 8, 9)

#User Instructions
print ("Let's multiple " + str(tup1[0]) + " by " + str(tup2[0]))
print ("What do you think the answer is? ")

#User Input
user_answer = input()
#Correct Answer
correct_answer = (tup1[0]*tup2[0])

#Grade user's guess
if str(user_answer) == str(correct_answer):
    print ("Congrats! You were right!")
else:
    print ("Oops. Incorrect")
