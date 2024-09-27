salary=input("Hello please enter your monthly salary :")


if float(salary)>=30000.00:
    print("You are elligible for the loan!")
else:
    print("Unfortunately your salary is too low to avail a loan.")
    exit()

loan=input("Please Enter the amount that you want to Loan :")

if float(loan)>=float(salary)*10:
    print("Sorry but the loan is too big")
else:
    input("How many months do you want to pay the loan for? :")
print(float(loan) + float(loan)*.10)
