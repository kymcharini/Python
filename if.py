# if statement
x=1
marks=50
grade=20
quantity=15
day=2
if(x>0):
    print("The number is positive")
# if... else statement
if(marks>=50):
    print("You have passed the exam")
else:
    print("You have failed the exam")
    # if .. elif...else statement
if(grade>=29 and grade<=0):
    print("You failed")
elif grade<=30 and grade>=49:
    print("You have passed")
elif(grade>=50 and grade>=79):
    print("You have a credit")
elif(grade<=80 and grade >=100):
    print("You have a distinction")
else:
    print("Wrong grade entered")

# if...elif...else statement
if quantity>=6 and quantity<=0:
    print("Very few")
elif quantity<=14 and quantity>=50:
    print("Add more")
elif quantity <=80 and quantity >=100:
    print("Excellent")
else:
    print("Purchase again")

if quantity>=6 and quantity<=15:
    print("Not yet")
elif quantity<=14 and quantity>=50:
    print("Mmmh")
else:
    print("Done")