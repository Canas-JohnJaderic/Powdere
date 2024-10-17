#Misc shayt
name=input("Please Enter the Student Name ")
section=input("Please Enter the Students Section ")

prelim=float(input("Enter Preliminary Grade: "))
midterm=float(input("Enter Mid Term Grade: "))
last=float(input("Enter Final Period Grade: "))

#Computations reyal
final=float(prelim) + float(midterm) + float(last)
pakerfinal=float(final)/3
reyalfinal=round(pakerfinal)



#Conditionals pake
if prelim<40 or prelim>100:
    print("Invalid Prelim Grade")
if midterm<40 or midterm>100:
    print("Invalid MidTerms Grade")
if last<40 or last>100:
    print("Invalid Final Period Grade")    
else:
    print("You have entered valid Grades, please wait while we calculate it for you")   

#Super Idol的笑容 都没你的甜 八月正午的阳光 都没你耀眼 热爱 105 °C的你 滴滴清纯的蒸馏水

if 78>reyalfinal>=75:
    print(f"You Passed your grade is: {reyalfinal}\n GPA: 3.00 ")
elif 81>reyalfinal>=78:
    print(f"You passed with the rating of Fair, your Grade is: {reyalfinal}\n GPA: 2.75")
elif 84>reyalfinal>=81:
    print(f"You have passed with the rating of Fairly Satisfactory, your Grade is: {reyalfinal}\n GPA: 2.50")
elif 87>reyalfinal>=84:
    print(f"You have passed with the rating of Satisfactory, your Grade is: {reyalfinal}\n GPA: 2.25 ")
elif 90>reyalfinal>=87:
    print(f"You have passed with the rating of Good, your Grade is: {reyalfinal}\n GPA: 2.00 ")
elif 93>reyalfinal>=90:
    print(f"You have passed with the rating of Very Good, your Grade is: {reyalfinal}\n GPA: 1.75 ")
elif 96>reyalfinal>=93:
    print(f"You have passed with the rating of Superior, your Grade is: {reyalfinal}\n GPA: 1.50 ")
elif 99>reyalfinal>=96:
    print(f"You have passed with the rating of Outstanding, your Grade is: {reyalfinal}\n GPA: 1.25 ")
elif 100>reyalfinal>=99:
    print(f"Wow! You passed with the rating of Excellent, your Grade is: {reyalfinal}\n GPA: 1.00")
else:
    print("Unfortunately you Failed")
