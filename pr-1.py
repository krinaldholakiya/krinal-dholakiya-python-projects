print("welcome to the personal data collector.\n")

a=input("please enter your name:")
b=int(input("please enter your age:"))
c=float(input("please enter your height in meters:"))
d=int(input("please enter your favorite number:"))

print("\nthank you! here is the information we collected:\n")

print("Name:",a,"",type(a),",memory address:",id(a))
print("Age:",b,"",type(b),",memory address:",id(b))
print("height:",c,"",type(c),",memory address:",id(c))
print("favorite number:",d,"",type(d),",memory address:",id(d))

print("\nyour birth year is approximetly:",2026-b)

print("\nthank you for using personal data collector,goodbye!")
