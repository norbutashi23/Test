print("Newton's Second Law of Motion")
print("Select the missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input ("Enter the option numberfor the missing value: ")
if missing_value_choice == "1":
    a = float(inpurt("Enter acceleration (a): "))
    F = float(input("Enter force (f): "))
    m = F / a
    print(f"Ma[ss (m) = {m}")
    
elif missing_value_choice == "2":
    m =float(input("Enter mass (m): "))
    F = float(input("Enter force (F):"))
    a = F / m
    print(f"Acceleration (a) = {a}")
    
else:
    print("invalid option selected for the missing value.")
