import sympy as sy

def x_expr_integrate(
    x_expr: str,
    x_lower: float = None,
    x_upper: float = None,
):
    integral_value = None
    x = sy.symbols("x")
    expr = sy.sympify(x_expr.lower())
    expr_integral = sy.integrate(
        expr, x
    )

    if x_lower and x_upper:
        integral_value = sy.integrate(
            expr, (x, x_lower, x_upper)
        )
    return (
        str(expr_integral),
        integral_value,
    )


integral, val = x_expr_integrate(
    "x**2+x*4+2+1/x+sin(x)", 1.00, 2.00
)
print("Integral = " + integral)
print("Definite Integral Value = " + str(val))
