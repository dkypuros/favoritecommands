#import standard library
import random
from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="yellow")
button3 = Button(topFrame, text="Button 3", fg="orange")
button4 = Button(bottomFrame, text="Button 4", fg="green")

print ("Hello world")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()

# Multiplication Tables
tup1 = (3, 4, 5, 6, 7, 8, 9)
tup2 = (3, 4, 5, 6, 7, 8, 9)
#Random multiplication fact to test user
roll1 = random.randint(0, 6)
roll2 = random.randint(0, 6)

#User Instructions
print ("Let's multiple " + str(tup1[roll1]) + " by " + str(tup2[roll2]))
print ("What do you think the answer is? ")

#User Input
user_answer = input()
#Correct Answer
correct_answer = (tup1[roll1]*tup2[roll2])

#Grade user's guess
if str(user_answer) == str(correct_answer):
    print ("Congrats! You were right! The Correct answer is: " + str(correct_answer))
else:
    print ("Oops. Incorrect. The Correct answer is: " + str(correct_answer))
