import math as m
import matplotlib.pyplot as plt

# length
L = m.pi

# number of points
n = 17

# delta x
dx = L / n

# delta t (time difference)
dt = 0.2

# simple string oscillation function
sin = m.sin


def foo():
    global n
    n = n + 1
    result_y = list()
    result_v = list()
    x_i = [0] * n
    y = [0] * n
    y_mid = [0] * n
    v = [0] * n
    v_mid = [0] * n
    a = [0] * n
    a_mid = [0] * n
    for i in range(n):
        x_i[i] = x_i[i - 1] + dx
        if i == 0:
            x_i[i] = 0
        y[i] = sin(x_i[i])
        if i == n - 1:
            y[i] = 0

    result_y.append(y.copy())
    result_v.append(v.copy())

    # main loop
    for k in range(n - 1):

        # calculating a
        for i in range(1, n - 1, 1):
            a[i] = (y[i + 1] - 2 * y[i] + y[i - 1]) / dx ** 2

        # calculating v_mid
        for i in range(1, n, 1):
            v_mid[i] = v[i] + a[i] * dt / 2

        # calculating y_mid
        for i in range(1, n, 1):
            y_mid[i] = y[i] + v[i] * dt / 2

        # calculating a_mid
        for i in range(1, n - 1, 1):
            a_mid[i] = (y_mid[i + 1] - 2 * y_mid[i] + y_mid[i - 1]) / dx ** 2

        # calculating v
        for i in range(1, n, 1):
            v[i] += a_mid[i] * dt

        # calculating y
        for i in range(1, n, 1):
            y[i] += v_mid[i] * dt

        result_y.append(y.copy())
        result_v.append(v.copy())

    return x_i, result_y, result_v


x, result_y, result_v = foo()

for y in result_y:
    plt.plot(x, y)

plt.show()

E_k = list()
for i in result_v:

    E_k_sum = 0
    for j in i:
        E_k_sum += j ** 2
    E_k_sum *= dx / 2
    E_k.append(E_k_sum)

plt.plot(x, E_k)

E_p = list()
for i in result_y:
    E_p_sum = 0
    for j in range(len(i)):
        E_p_sum += (i[j] - i[j - 1]) ** 2
    E_p_sum *= 1 / (2 * dx)
    E_p.append(E_p_sum)

plt.plot(x, E_p)

E_t = list()
for i in range(len(x)):
    E_t.append(E_k[i] + E_p[i])

plt.plot(x, E_t)
plt.show()
