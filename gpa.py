marks = float(input("Enter your marks : "))
if(marks > 100):
    print("Try again")
elif(marks==100 or marks >= 80):
    print("A+")
elif(marks=<80 or marks >= 70):
    print("A")
elif(marks<=70 or marks >= 60):
    print("A-")
elif(marks<=60 or marks >= 50):
    print("B")
else:
    print("Fail")