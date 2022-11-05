import sympy as sy


def x_expr_diff(
    x_expr: str, x_value: float
):
    expr = sy.sympify(x_expr.lower())
    expr_diff = sy.diff(expr, "x")
    x = sy.symbols("x")
    return (
        str(expr_diff),
        expr_diff.subs(x, x_value),
    )


diff, val = x_expr_diff(
    "x**2+x*4", 1.00
)
print("Derivative = " + diff)
print("Derivative Value = " + str(val))

diff, val = x_expr_diff(
    "cos(x**2)", 0.0
)
print("Derivative = " + diff)
print("Derivative Value = " + str(val))
