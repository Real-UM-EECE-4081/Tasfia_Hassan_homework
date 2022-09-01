#question 05

f0 = 1
f1 = 1

print("Fibonacci series between 0 to 50: ")

while f0 <= 50:
    print(f0, end=' ')
    f = f0 + f1
    f0 = f1
    f1 = f
print()
