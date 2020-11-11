from typing import List
import sympy
import numpy as np
import pandas as pd

__all__ = ['M', 'simplex', 'rationals']

COLUMN = 80
# 罰金法のM
M = sympy.Symbol('M')
_real_M = 1e10
subs_all = np.vectorize(lambda e: e.subs({M: _real_M}))


def rationals(a):
    result = []
    for e in a:
        if isinstance(e, list):
            result.append(rationals(e))
        elif isinstance(e, sympy.Basic):
            result.append(e)
        else:
            result.append(sympy.Rational(e))
    return result


def pretty_print(c, c_name, m, base, base_name, pi, c_pi, theta=None):
    df = pd.DataFrame([
        ['', 'c', *list(c), '', ''],
        ['base', 'base_name', *list(c_name), 'const', 'theta'],
        *[
            [_base, _base_name, *list(_m), _theta]
            for _base, _base_name, _m, _theta in zip(base, base_name, m,  ['']*len(base_name) if theta is None else theta)
        ],
        ['', 'pi', *list(pi), ''],
        ['', 'c - pi', *list(c_pi), '', '']
    ], columns=None)
    print(df.to_string(index=False, header=False))


def step(MAX, c, c_name, m, base, base_name):
    pi = base @ m
    c_pi = c - pi[:-1]

    # print('pi', pi)
    # print('c - pi', c_pi)

    # 終了条件
    _subs_c_pi = subs_all(c_pi)
    if MAX:
        finish = np.all(_subs_c_pi <= 0)
    else:
        finish = np.all(_subs_c_pi >= 0)

    if finish:
        pretty_print(c, c_name, m, base, base_name, pi, c_pi)
        # print(base_name)
        # print(base)
        # print(m)
        # print('finish')
        print()

        for i, _c_name in enumerate(c_name):
            if _c_name in base_name:
                print(f'{_c_name} = {m[:,-1][base_name.index(_c_name)]}')
            else:
                print(f'{_c_name} = {0}')
        print(f'{"max" if MAX else "min"} = {pi[-1]}')
        return False

    # ピボット決定
    if MAX:
        piv_col = np.argmax(_subs_c_pi)
    else:
        piv_col = np.argmin(_subs_c_pi)

    # <=0 で割るときは無視
    _div = m[:, piv_col]
    _pos_mask = np.where(_div > 0)
    theta = np.array([sympy.Rational(0)] * _div.shape[0])
    theta[_pos_mask] = m[:, -1][_pos_mask] / _div[_pos_mask]
    theta[np.where(_div <= 0)] = np.inf
    # print('theta', theta)
    piv_row = np.argmin(theta)

    pretty_print(c, c_name, m, base, base_name, pi, c_pi, theta)
    print(f'pivot(col = {c_name[piv_col]}, row = {base_name[piv_row]})')

    # 係数・基底変数入れ替え
    base[piv_row] = c[piv_col]
    base_name[piv_row] = c_name[piv_col]

    # ガウスジョルダンの掃き出し法
    m[piv_row] = m[piv_row] / m[piv_row, piv_col]
    for i, b in enumerate(base_name):
        if i != piv_row:
            m[i] = m[i] - m[i, piv_col] * m[piv_row]

    # print('='*COLUMN)
    # print(base_name)
    # print(base)
    # print(m)

    return True


def simplex(MAX: int, c: np.ndarray, c_name: List[str], m: np.ndarray, base: np.ndarray, base_name: List[str]):

    if c.shape[0] != len(c_name):
        print('c and c_name shape do not match')
        return False
    if base.shape[0] != len(base_name):
        print('base and base_name shape do not match')
        return False
    if m.shape[1] != c.shape[0] + 1:
        print('m or c shape is invalid')
        return False

    # print(c)
    # print(c_name)
    # print('-'*COLUMN)
    # print(base)
    # print(base_name)
    # print(m)

    while step(MAX, c, c_name, m, base, base_name):
        print('-'*COLUMN)
