import numpy as np
from simplex import simplex, rationals

if __name__ == "__main__":
    # max = True, min = False
    MAX = False
    # 目的関数係数
    c = np.array(rationals([0, 0, 0, 0, 0, 1, 1, 1]))
    c_name = [f'x{i+1}' for i in range(len(c))]

    # 制約条件係数行列
    m = np.array(rationals([
        [1, 2, 1, 0, 0, 1, 0, 0, 20],
        [7, 6, 0, -1, 0, 0, 1, 0, 84],
        [1, -1, 0, 0, 1, 0, 0, 1, 8],
    ]))

    # 基底変数
    base_name = ['x6', 'x7', 'x8']
    base = np.array([c[c_name.index(e)] for e in base_name])

    simplex(MAX, c, c_name, m, base, base_name)
