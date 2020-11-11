from typing import List
import numpy as np
from simplex import simplex, rationals
import sys
import sympy


def scanlist():
    line = sys.stdin.readline().strip()
    if len(line):
        return list(map(lambda e: e.strip(),
                        line.split(',')))
    else:
        return []


def strlist2rationals(src: List[str]):
    return list(map(lambda e: sympy.Rational(*map(int, e.split('/'))), src))


if __name__ == "__main__":
    MAX = input('最大化 or 最小化 (max or min)') == 'max'
    # 目的関数係数
    print('目的関数係数')
    c = np.array(strlist2rationals(scanlist()))
    c_name = [f'x{i+1}' for i in range(len(c))]

    # 制約条件係数行列
    print('制約条件係数行列 (空行で完了)')
    keisu = []
    while True:
        l = strlist2rationals(scanlist())
        if len(l) == 0:
            break
        else:
            keisu.append(l)

    m = np.array(keisu)

    # 基底変数
    print('基底変数')
    base_name = scanlist()
    base = np.array([c[c_name.index(e)] for e in base_name])

    simplex(MAX, c, c_name, m, base, base_name)
