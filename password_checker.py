password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    print("Password length: Good")
    score += 1
else:
    print("Password lenghth: Too short")

if any(char.isupper() for char in password):
    print("Uppercase letter: Found")
    score += 1

if any(char.islower() for char in password):
    print("Lowercase letter: Found")
    score += 1

if any(char.isdigit() for char in password):
    print("Number: Found")
    score +=1

if any(not char.isalnum() for char in password):
    print("Special character: Found")
    score += 1

print("Password Score:", score, "/ 5")    

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Strong")
