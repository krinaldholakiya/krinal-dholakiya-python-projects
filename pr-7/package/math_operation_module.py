import math

def factorial_number():
    print()
    n=int(input("Enter Any Number: "))
    if n<0:
        print("Factorials are mathematically undefined for negative numbers.")
    else:
        fact=math.factorial(n)
    print(f"The Factorial of {n} is {fact}.")
    print()
                     
def compound_interest():
    print()      
    print("===============================================")
    p = float(input("\nEnter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = float(input("Enter time (in years): ")) 
    amount = p * ((1 + r / 100) **t)
    print(f"Compound Interest: {amount:.2f}")
    print("===============================================")

    print()
                    
def trigonometry():
    angle = float(input("\nEnter angle in degrees: "))
    rad = math.radians(angle)
    print(f"sin({angle}) = {math.sin(rad):.4f}")
    print(f"cos({angle}) = {math.cos(rad):.4f}")
    if angle % 180 == 90:
        print(f"tan({angle}) = Undefined")
    else:
        print(f"tan({angle}) = {math.tan(rad):.4f}")
    print("===============================================")
    print()

def  area_Rectangle():
    print() 
    l = float(input("Length: "))
    b = float(input("Breadth: "))
    print()
    print("Area Of Rectangle =", l * b)
    print()

def area_Square():
    print()
    s = float(input("Side: "))
    print()
    print("Area Of Square =", s * s)
    print()  

def area_triangle():
    print()
    b = float(input("Base: "))
    h = float(input("Height: "))
    print()
    print("Area Of Triangle =", 0.5 * b * h)
    print()    

def area_circle():
    print()
    r = float(input( "Radius: "))
    print()
    print("Area Of Circle =", math.pi * r * r)
    print()