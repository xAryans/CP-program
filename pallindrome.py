A = int(input("Enter a number: "))

rev = int(str(A)[::-1])

if A == rev:
    print("Yes")
else:
    print("No")
