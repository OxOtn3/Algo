# 用来快速求解函数零点，从而求解平方根
def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    
    C, x0 = float(x), float(x)
    while True:
        xi = 0.5 * (x0 + C / x0)
        if abs(x0 - xi) < 1e-7:
            break
        x0 = xi
    
    return int(x0)