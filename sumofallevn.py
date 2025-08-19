A = int(input("Enter a integer: "))
sum = 0
for i in range(2, A + 1, 2):
    if i % 2 == 0:
        sum += i
print("The sum of all even numbers up to", A, "is:", sum)
