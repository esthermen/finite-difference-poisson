import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import time


def solve_poisson(XN, xf=9, zf=0.5, Q=0.6, k=0.16, H=0.073, ur=25, gf=-15, eps=1e-5):
    """
    Solves the 2D Poisson equation using finite differences
    with mixed boundary conditions.
    """

    YN = XN // 2
    h = xf / XN

    d = zf * 1e-2
    f = Q / (k * d)

    T = np.zeros((YN, XN))
    T_prev = np.ones((YN, XN))

    # Dirichlet boundaries (left & right)
    T[:, 0] = 20
    T[:, -1] = 20

    while norm(T - T_prev) > eps:
        T_prev = T.copy()

        for y in range(YN):
            for x in range(1, XN - 1):

                if y == 0:  # bottom boundary
                    go = H * (T[y, x] - ur) / k
                    T[y, x] = 0.25 * (
                        2 * T[1, x]
                        + T[0, x - 1]
                        + T[0, x + 1]
                        - h**2 * f
                        - 2 * h * go
                    )

                elif y == YN - 1:  # top boundary
                    T[y, x] = 0.25 * (
                        2 * T[YN - 2, x]
                        + T[y, x - 1]
                        + T[y, x + 1]
                        - h**2 * f
                        - 2 * h * gf
                    )

                else:  # interior
                    T[y, x] = 0.25 * (
                        T[y - 1, x]
                        + T[y + 1, x]
                        + T[y, x - 1]
                        + T[y, x + 1]
                        - h**2 * f
                    )

    return T


if __name__ == "__main__":
    resolutions = [8, 16, 32, 64]

    for XN in resolutions:
        start = time.time()
        T = solve_poisson(XN)
        end = time.time()

        print(f"Resolution {XN}x{XN//2} solved in {end - start:.4f} s")

        plt.imshow(T, cmap="gray", origin="lower")
        plt.title(f"Poisson solution ({XN}x{XN//2})")
        plt.colorbar(label="Temperature")
        plt.show()
