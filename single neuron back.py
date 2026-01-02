x = [1, -2, 3]
w = [-3, -1, 2.0]
b = 1

xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]

print(xw0, xw1, xw2, b)

z = xw0 + xw1 + xw2 + b
print(z)

y = max(z, 0)
print(y)