#it based on ifelse condition calculator
first=input("enter first number: ")
operator =input("enter operator(+,-,/,*,%): ")
second=input("enter second number: ")
first=int(first) # coverting str to int
second=int(second) # same as above
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
elif operator=="*":
    print(first**second)
else:
    print("invalid operation")