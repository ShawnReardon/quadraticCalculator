// Adpated from https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/
function getInput () {
    // Driver Program
    a = game.askForNumber("A = ")
    b = game.askForNumber("B =")
    c = game.askForNumber("C =")
    // If a is 0, then incorrect equation
    if (a == 0) {
        console.log("Input correct quadratic equation")
        game.showLongText("Input correct quadratic equation", DialogLayout.Top)
        getInput()
    } else {
        equationroots(a, b, c)
    }
}
// function for finding roots
function equationroots (a: number, b: number, c: number) {
    // calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = Math.sqrt(Math.abs(dis))
    // checking condition for discriminant
    if (dis > 0) {
        console.log(" real and different roots ")
        console.log((0 - b + sqrt_val) / (2 * a))
        console.log((0 - b - sqrt_val) / (2 * a))
        game.showLongText(" real and different roots " + ("" + (0 - b + sqrt_val) / (2 * a)) + " or " + ("" + (0 - b - sqrt_val) / (2 * a)), DialogLayout.Top)
    } else if (dis == 0) {
        console.log(" real and same roots")
        console.log((0 - b) / (2 * a))
        game.showLongText(" real and same roots" + "" + ("" + (0 - b) / (2 * a)), DialogLayout.Top)
    } else {
        // when discriminant is less than 0
        console.log("Complex Roots")
        console.log("" + (0 - b) / (2 * a) + " + i" + ("" + sqrt_val))
        console.log("" + (0 - b) / (2 * a) + " - i" + ("" + sqrt_val))
        game.showLongText("" + (0 - b) / (2 * a) + " - i" + ("" + sqrt_val) + " or" + ("" + (0 - b) / (2 * a) + " + i" + ("" + sqrt_val)), DialogLayout.Top)
    }
}
let sqrt_val = 0
let dis = 0
let c = 0
let b = 0
let a = 0
getInput()
