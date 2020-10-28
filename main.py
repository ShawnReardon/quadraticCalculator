# function for finding roots
def equationroots(a: number, b: number, c: number):
    global dis, sqrt_val
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = Math.sqrt(abs(dis))
    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((0 - b + sqrt_val) / (2 * a))
        print((0 - b - sqrt_val) / (2 * a))
    elif dis == 0:
        print(" real and same roots")
        print((0 - b) / (2 * a))
            # when discriminant is less than 0 
    else:
        print("Complex Roots")
        print(- b / (2 * a) + " + i" + sqrt_val)  
        print(- b / (2 * a) + " - i" + sqrt_val)
sqrt_val = 0
dis = 0
# Driver Program
a = game.ask_for_number("A = ")
b = game.ask_for_number("B =")
c = game.ask_for_number("C =")
# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")
else:
    equationroots(a, b, c)



