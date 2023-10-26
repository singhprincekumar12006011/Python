# WAP to print massege of scholorship got by the user based on there marks.
# take the marks as input from user.

x=float(input("Enter you marks:\n"))

if x >= 80:
    print("You will get 30% scholarship\n")
elif 80 > x >= 70:
    print("You will get 20% schoralship:\n")
elif 70 > x >=60:
    print("You will get 10% schoralship:\n")
elif x < 60:
    print("Sorry!, You are not eligible for scholarship:\n")