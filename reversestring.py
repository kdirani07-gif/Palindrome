name=input("What is your name")
last_index=len(name)-1

# initialize an empty string to store the reverse word
reversed=""

# reverse using the for loop
for i in range(last_index,-1,-1):
    reversed += name[i]

print(f"Your name backwards is {reversed}")