print("enter the mark obtained in each subject")
eng=int(input("Enter english mark"))
math=int (input("Enter math mark"))
science= int (input("Enter science mark"))
gym= int (input("Enter gym mark"))
history=int (input("Enter history mark"))
total=eng+math+science+gym+history
abg=total/5
print("Your average is",abg)
if abg>=91 and abg<=100:
    print("Your Grade is A1")
elif abg>=81 and abg<=91:
    print("Your grade is A2")
elif abg>=71 and abg<=81:
    print("Your grade is B1")
elif abg>=61 and abg<=71:
    print("your average is B2")
elif abg>=51 and abg<=61:
    print("Your average is C1 ")
elif abg>=41 and abg<=51:
    print("Your average is C2")
elif abg>=31 and abg<=41:
    print("Your average is D1")
elif abg>=21 and abg<=31:
    print("Your average is D2")
elif abg>=11 and abg<=21:
    print("Your average is E1")
elif abg>=1 and abg<=11:
    print("Your average is E2")
else:
    print("invaild input")