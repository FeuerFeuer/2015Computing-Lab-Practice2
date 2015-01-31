running = True
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
if n1 < n2:
    d = n1
else:
    d = n2


while running:
    if n1 % d == 0 and n2 % d == 0:
        print(d)
        running = False

    d = d - 1
