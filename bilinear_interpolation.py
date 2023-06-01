from linear_interpolation import linear_interpolation


def bilinear_interpolation(x, y, f, x0, y0):
    f1 = (x[1] - x0) / (x[1] - x[0]) * f[0][0] + (x0 - x[0]) / (x[1] - x[0]) * f[1][0]
    f2 = (x[1] - x0) / (x[1] - x[0]) * f[0][1] + (x0 - x[0]) / (x[1] - x[0]) * f[1][1]

    f = (y[1] - y0) / (y[1] - y[0]) * f1 + (y0 - y[0]) / (y[1] - y[0]) * f2

    return f
