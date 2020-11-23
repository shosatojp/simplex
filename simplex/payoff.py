from simplex import simplex, rationals
import numpy as np
import sympy
if __name__ == "__main__":
    import util
else:
    from . import util


def optimal_policy(a: np.ndarray):
    # w > 0とするためにすべて1以上に
    C = -min(1, np.min(a)) + 1

    # yからもとめる
    c = np.concatenate([np.ones((a.shape[1],)), np.zeros((a.shape[0],))])
    c_name = [f'y{i+1}' for i in range(a.shape[1] + a.shape[0])]
    m = np.concatenate([a + C, np.eye(a.shape[0]), np.ones((a.shape[0], 1))], axis=1)
    base = np.zeros((a.shape[0],))
    base_name = c_name[a.shape[1]:]

    m, base, base_name = simplex(1,
                                 np.array(rationals(c)),
                                 c_name,
                                 np.array(rationals(m)),
                                 np.array(rationals(base)),
                                 base_name)

    _ans = base.T @ m[:, -1]
    w = 1/_ans - C

    print('------- optimal policy -------')

    eqs = []
    for i, _c_name in enumerate(c_name[:a.shape[1]]):
        yi = m[:, -1][base_name.index(_c_name)] if _c_name in base_name else 0

        if yi != 0:
            eqs.append(np.concatenate([(a + C)[:, i], [sympy.Rational(1)]]))

        print(f'y{i + 1}* = {yi / _ans}')

    eqs.append(np.array([sympy.Rational(1)] * a.shape[0] + [_ans]))

    if len(eqs) < a.shape[0]:
        print('Error: lack of equations')

    x = util.solve(np.array(eqs)[:a.shape[0]])

    for i in range(a.shape[0]):
        print(f'x{i + 1}* = {x[i,-1] / _ans}')

    print(f'w = {w}')


if __name__ == "__main__":
    a = np.array(rationals([
        [2, -3, -4],
        [-6, -1, 1],
    ]))

    a = np.array(rationals([
        [3, 5],
        [-3, 4],
        [7, -6],
    ]))

    optimal_policy(a)
