number = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit up which you want the multiplication table generated: "))

for i in range(1, limit + 1):
    print(f"{number} * {i} = {number * i}")