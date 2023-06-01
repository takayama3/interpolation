def linear_interpolation(x, y, x0):
    return y[0] + (y[1] - y[0]) / (x[1] - x[0]) * (x0 - x[0])
