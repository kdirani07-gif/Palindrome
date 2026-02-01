s = "Learning"
print(s.lower())
print(s.upper())
S = "Qwerty00"
password = input("What is the password?")
# does password contain 2 digits
# i will look for every character one by one and i will store it in a variable
print(len(password))
digits = 0
for i in range(len(password)):
    if password [i].isdigit():
        # increase the count of digits
        digits+=1

print(digits)
if digits >= 2:
    print("Password is Valid.")
else:
    print("Password is Invalid.")
