import calculator as cl

def hypotenuse(x, y):
    hyp = cl.sqrt(
            cl.mySum(
                cl.myProd(x, x),
                cl.myProd(y, y)
                )
            )
    return hyp

x = 3
y = 4
print(hypotenuse(3, 4))
