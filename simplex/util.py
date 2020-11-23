import numpy as np


def solve(a: np.ndarray):
    # ガウスジョルダンの掃き出し法
    for piv in range(a.shape[0]):
        a[piv] = a[piv] / a[piv][piv]
        for i in range(piv + 1, a.shape[0]):
            a[i] -= a[i][piv] * a[piv]

    for piv in range(a.shape[0] - 1, -1, -1):
        for i in range(piv - 1, -1, -1):
            a[i] -= a[i][piv] * a[piv]

    return a
