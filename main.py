# Adpated from https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/

def getInput():
    global a, b, c
    # Driver Program
    a = game.ask_for_number("A = ")
    b = game.ask_for_number("B =")
    c = game.ask_for_number("C =")
    # If a is 0, then incorrect equation
    if a == 0:
        print("Input correct quadratic equation")
        game.show_long_text("Input correct quadratic equation", DialogLayout.TOP)
        getInput()
    else:
        equationroots(a, b, c)
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
        game.show_long_text(" real and different roots " + str((0 - b + sqrt_val) / (2 * a)) + " or " + str((0 - b - sqrt_val) / (2 * a)),
            DialogLayout.TOP)
    elif dis == 0:
        print(" real and same roots")
        print((0 - b) / (2 * a))
        game.show_long_text(" real and same roots" + "" + str((0 - b) / (2 * a)),
            DialogLayout.TOP)
    else:
        # when discriminant is less than 0
        print("Complex Roots")
        print("" + str((0 - b) / (2 * a)) + " + i" + str(sqrt_val))
        print("" + str((0 - b) / (2 * a)) + " - i" + str(sqrt_val))
        game.show_long_text("" + str((0 - b) / (2 * a)) + " - i" + str(sqrt_val) + " or" + ("" + str((0 - b) / (2 * a)) + " + i" + str(sqrt_val)),
            DialogLayout.TOP)
sqrt_val = 0
dis = 0
c = 0
b = 0
a = 0
getInput()