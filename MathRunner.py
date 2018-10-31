#!/usr/bin/python

from MathTricks import *
import time
from __builtin__ import exit
#Omitted inst1 because it's redundant and confusing. Just printing the text is more streamline as it's not used twice.
print "Math Trick 1\n\
		1. Pick a number less than 10\n\
		2. Double the number\n\
		3. Add 6 to the answer\n\
		4. Divide the answer by 2\n\
		5. Subtract your original number from the answer\n"


# Get input for the first math trick
num = raw_input("Enter a number less than 10: ")
if num == "GramPacer Test":
    print "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
    exit()
else:
    num = int(num)
# Call the trick1 method within a print statement to print the result
time.sleep(.2)
print "Your answer is", trick1(num), "\n\n"

time.sleep(2)

#Second trick
#Omitted inst2 because it's redundant and confusing. Just printing the text is more streamline as it's not used twice.
print "Math Trick 2\n\
		1. Pick any number\n\
		2. Multiply the number by 3\n\
		3. Add 45 to the answer\n\
		4. Multiple the answer by 2\n\
		5. Divide the answer by 6\n\
		6. Subtract your original number from the answer\n"


# Get input for the second math trick
time.sleep(.2)
num2 = input("Enter any number: ")

# Call the trick2 method within a print statement to print the result

print "Your answer is", trick2(num2), "\n\n"

time.sleep(3)

print "Thank you for using code created by Anand. If you would like to buy more code, you may purchase it at 7hills.org/best-developer-ever"
