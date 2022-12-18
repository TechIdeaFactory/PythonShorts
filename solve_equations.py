from sympy import (
    symbols,
    sympify,
    solve,
)

sy_eq_list = []
x = symbols("x")
y = symbols("y")

while True:
    eq = input(
        "Enter x and y var eqn "
        "or 'S' to solve"
    )
    eq = eq.lower()

    if eq == "s":
        sol = solve(
            tuple(sy_eq_list), (x, y)
        )
        print("Solution " + str(sol))

        break
    else:
        sy_eq = sympify(eq)
        sy_eq_list.append(sy_eq)
