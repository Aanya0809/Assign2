l1 = float(input("Enter length of side 1: "))
l2 = float(input("Enter length of side 2: "))
l3 = float(input("Enter length of side 3: "))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print("Yes")
else:
    print("No")